#!/usr/bin/env python3
"""Soumet toutes les URLs de la doc à IndexNow (Bing/Yandex + partenaires).

IndexNow prévient instantanément les moteurs qu'une page a été ajoutée/modifiée,
au lieu d'attendre le prochain crawl. Complète Cloudflare Crawler Hints (activé
sur lplg.eu, mais moins fiable pour la doc servie par le Worker en cache-bypass).

Prérequis : le fichier-clé doit être EN LIGNE (donc pousser le repo d'abord) :
    https://www.lplg.eu/resthome/documentation/d9ca9e04132841a2a43b7bd734cd88e8.txt

Usage (après déploiement) :
    .venv/Scripts/python.exe docs-ops/submit-indexnow.py

À relancer après chaque mise à jour de contenu de la doc.
"""
import json
import re
import urllib.request

HOST = "www.lplg.eu"
KEY = "d9ca9e04132841a2a43b7bd734cd88e8"
KEY_LOCATION = f"https://{HOST}/resthome/documentation/{KEY}.txt"
SITEMAP = "https://www.lplg.eu/resthome/documentation/sitemap.xml"
ENDPOINT = "https://api.indexnow.org/IndexNow"


def get_urls() -> list[str]:
    with urllib.request.urlopen(SITEMAP, timeout=30) as r:
        xml = r.read().decode("utf-8")
    return re.findall(r"<loc>([^<]+)</loc>", xml)


def submit(urls: list[str]) -> None:
    payload = json.dumps({
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=payload,
        headers={"Content-Type": "application/json; charset=utf-8"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"IndexNow -> HTTP {resp.status} ({len(urls)} URLs soumises)")
    except urllib.error.HTTPError as e:
        codes = {
            400: "format invalide",
            403: "clef non valide (fichier-clef en ligne ? pousser le repo d'abord)",
            422: "URLs hors du host ou clef non conforme",
            429: "trop de requetes",
        }
        print(f"IndexNow -> HTTP {e.code} : {codes.get(e.code, e.reason)}")


def main() -> None:
    urls = get_urls()
    print(f"{len(urls)} URLs trouvees dans le sitemap.")
    submit(urls)
    print("Verifier la reception dans Bing Webmaster Tools (section IndexNow).")


if __name__ == "__main__":
    main()
