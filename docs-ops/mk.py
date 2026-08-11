#!/usr/bin/env python3
"""Sous-commandes du Makefile qui auraient besoin d'un shell POSIX.

POURQUOI CE FICHIER : sous Windows, `make` lance **cmd.exe**, qui ne connaît ni
`test`, ni `rm`, ni les accolades de regroupement, affiche les guillemets de
`echo "..."` littéralement et mange les caractères non-ASCII (son codepage
n'est pas UTF-8). Un Makefile écrit en POSIX y échoue ligne après ligne.

Tout ce qui dépasse « lancer un programme » vit donc ici, en Python — présent
par construction (c'est l'interpréteur du venv qui bâtit la doc), et identique
sur Windows, Linux et macOS.

    python docs-ops/mk.py help
    python docs-ops/mk.py preview --port 8010
    python docs-ops/mk.py live    --live-port 8011
    python docs-ops/mk.py clean
"""
import argparse
import functools
import http.server
import shutil
import socket
import socketserver
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def port_taken(port, host="127.0.0.1"):
    """Vrai si quelqu'un ECOUTE deja sur ce port.

    On tente une CONNEXION, pas un bind. Deux raisons, toutes deux propres a
    Windows :
      * `SO_REUSEADDR` y AUTORISE le bind sur un port deja pris (semantique
        inverse de POSIX) — une sonde qui l'active repond toujours « libre » ;
      * meme sans elle, Windows laisse binder `127.0.0.1:P` quand un autre
        socket ecoute sur `0.0.0.0:P`.
    Un bind reussi ne prouve donc rien. Une connexion qui aboutit, si.

    Sans ce controle, un port pris par un service systeme ne donne pas un
    « adresse deja utilisee » lisible mais un WinError 10013 (« acces au
    socket interdit »), qui n'evoque rien a la lecture.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as probe:
        probe.settimeout(0.4)
        return probe.connect_ex((host, port)) == 0


def refuse_busy_port(port, variable):
    sys.stderr.write(
        "Le port %d est indisponible (occupe, ou reserve par le systeme).\n"
        "Choisissez-en un autre :  make %s %s=%d\n"
        % (port, "preview" if variable == "PORT" else "live",
           variable, port + 1))
    return 1


HELP = """\
Documentation Resthome

  make serve       Construit le site puis le sert sur http://localhost:{port}
                   FR a la racine, /nl, /en - le site REEL, traductions comprises
  make preview     Sert le site DEJA construit, sans le reconstruire
  make live        Rechargement a chaud de la source EN sur http://localhost:{live}
                   Source anglaise uniquement - ne montre PAS les traductions

  make build       Construit ./site (les 3 langues) + statiques + sitemap
  make check       Controle les conventions de contenu
  make gettext     Re-extrait les POT et met a jour locale/{{fr,nl}}
  make pdf         Manuel PDF francais  (make pdf-nl pour le neerlandais)
  make publish     check + build + pdf - a passer avant de committer
  make clean       Supprime ./site et ./_build (les PDF versionnes sont gardes)

  Variables : PORT={port}  LIVE_PORT={live}
"""


def cmd_help(args):
    # Ecrit via sys.stdout.write plutot que print() : la console Windows est en
    # cp850, et un accent non gere ferait planter la cible `help`.
    sys.stdout.write(HELP.format(port=args.port, live=args.live_port))
    return 0


def cmd_preview(args):
    site = ROOT / "site"
    if not site.is_dir():
        sys.stderr.write(
            "./site est absent - lancez d'abord : make build\n")
        return 1
    if port_taken(args.port):
        return refuse_busy_port(args.port, "PORT")
    for label, path in (("francais", ""), ("neerlandais", "nl/"),
                        ("anglais", "en/")):
        sys.stdout.write(
            "-> http://localhost:%d/%-6s (%s)\n" % (args.port, path, label))
    sys.stdout.write("Ctrl+C pour arreter.\n")
    sys.stdout.flush()
    handler = functools.partial(http.server.SimpleHTTPRequestHandler,
                               directory=str(site))
    # allow_reuse_address : sans lui, un relancement immediat apres Ctrl+C
    # echoue avec « Address already in use » pendant la temporisation TIME_WAIT.
    class Server(socketserver.TCPServer):
        allow_reuse_address = True
    try:
        with Server(("", args.port), handler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        sys.stdout.write("\nArrete.\n")
    except OSError as exc:
        sys.stderr.write("Impossible d'ecouter sur le port %d : %s\n"
                         % (args.port, exc))
        return 1
    return 0


def cmd_live(args):
    # Invoque par -m plutot que par l'exe : le chemin de l'exe varie selon
    # l'OS (Scripts/ vs bin/) et son absence donne un « fichier introuvable »
    # opaque, la ou l'import dit clairement ce qui manque.
    try:
        from sphinx_autobuild.__main__ import main
    except ImportError:
        sys.stderr.write(
            "sphinx-autobuild n'est pas installe dans ce venv.\n"
            "Il est pourtant declare dans requirements.txt - le venv a derive.\n"
            "Installez-le seul (NE relancez pas tout requirements.txt : cela\n"
            "retrograderait Sphinx) :\n\n"
            "    %s -m pip install sphinx-autobuild\n" % sys.executable)
        return 1
    if port_taken(args.live_port):
        return refuse_busy_port(args.live_port, "LIVE_PORT")
    # --host/--port : la syntaxe `-a HOST:PORT` est celle des versions
    # anterieures a 2024 ; depuis, `-a` est transmis a Sphinx (« write all
    # files ») et l'adresse se donne par ces deux options. L'ancienne forme
    # echoue par « unrecognized arguments ».
    #
    # `site/` et `_publish/` sont ignores : ce sont des SORTIES du build. Sans
    # ca, reconstruire modifie ces dossiers, ce qui redeclenche un build — une
    # boucle sans fin.
    sys.argv = ["sphinx-autobuild", "-c", str(ROOT),
                str(ROOT / "content"), str(ROOT / "_build" / "live"),
                "--host", "127.0.0.1", "--port", str(args.live_port),
                "--ignore", str(ROOT / "site" / "*"),
                "--ignore", str(ROOT / "_publish" / "*")]
    return main()


def cmd_clean(args):
    """Ne supprime QUE des produits jetables et ignorés par git.

    Le manuel PDF de `_publish/` est VERSIONNÉ (c'est un livrable, pas du
    cache) : un `make clean` qui l'effacerait ferait apparaître une
    suppression dans `git status` — surprise désagréable et perte du fichier
    tant qu'on n'a pas relancé `make pdf`. Il reste donc en place.
    """
    removed = []
    for rel in ("site", "_build"):
        target = ROOT / rel
        if target.exists():
            shutil.rmtree(target, ignore_errors=True)
            removed.append(rel)
    sys.stdout.write("supprime : %s\n" % (", ".join(removed) or "(rien)"))
    sys.stdout.write(
        "Les PDF de _publish/ sont versionnes et donc conserves "
        "(make pdf pour les regenerer).\n")
    return 0


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("command",
                        choices=("help", "preview", "live", "clean"))
    parser.add_argument("--port", type=int, default=8010)
    parser.add_argument("--live-port", type=int, default=8011)
    args = parser.parse_args()
    return {"help": cmd_help, "preview": cmd_preview,
            "live": cmd_live, "clean": cmd_clean}[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
