#!/usr/bin/env python3
"""Génère le manuel Resthome en PDF, une langue par fichier.

CHAÎNE : Sphinx `singlehtml` (toutes les pages en un seul document, dans
l'ordre du toctree) puis le moteur d'impression de Chromium via Playwright.

Pourquoi pas LaTeX : `sphinx-build -b latex` exige une distribution TeX
complète (~4 Go, à maintenir sur chaque poste). Chromium est déjà installé
pour les captures, gère le CSS d'impression, la pagination et les liens
internes — et rend exactement ce que le lecteur voit sur le site.

    .venv/Scripts/python.exe build_pdf.py          # fr + nl
    .venv/Scripts/python.exe build_pdf.py fr       # une seule langue
"""
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "_publish"
LANGS = {"fr": "Manuel Resthome", "nl": "Resthome handleiding"}

# Le thème du site est fait pour l'écran : barres latérales, en-tête collant,
# bouton de recherche. À l'impression tout cela est du bruit — et la sidebar
# mangerait un tiers de chaque page.
PRINT_CSS = """
@page { size: A4; margin: 18mm 16mm 20mm 16mm; }
.md-header, .md-sidebar, .md-nav, .md-footer, .md-search,
.md-skip, .headerlink, .lplg-support-fab { display: none !important; }
.md-main__inner, .md-content, .md-grid { margin: 0 !important; max-width: none !important; }
body { font-size: 10.5pt; line-height: 1.45; }
/* Un chapitre = une page. Sans ça les titres tombent en bas de page. */
h1 { page-break-before: always; padding-top: 0; }
h1:first-of-type { page-break-before: avoid; }
h2, h3 { page-break-after: avoid; }
/* Ne jamais couper un tableau, un encadré ou une image en deux. */
table, .admonition, figure, img { page-break-inside: avoid; }
img { max-width: 100% !important; height: auto; }
pre { white-space: pre-wrap; word-wrap: break-word; font-size: 9pt; }
a { color: inherit; text-decoration: none; }
"""

HEADER = ('<div style="font-size:7pt;color:#888;width:100%;padding:0 16mm;'
          'text-align:right;">{title}</div>')
FOOTER = ('<div style="font-size:7pt;color:#888;width:100%;padding:0 16mm;'
          'text-align:center;">'
          '<span class="pageNumber"></span> / <span class="totalPages"></span>'
          '</div>')


def build_singlehtml(lang: str, dest: Path) -> Path:
    """Assemble toutes les pages en un seul document, dans l'ordre du toctree."""
    subprocess.run(
        [sys.executable, "-m", "sphinx", "-b", "singlehtml", "-c", str(ROOT),
         "-D", f"language={lang}", "-q", str(ROOT / "content"), str(dest)],
        check=True, cwd=ROOT)
    return dest / "index.html"


MERMAID_JS = (Path(__file__).resolve().parent / ".venv" / "Lib" /
              "site-packages" / "sphinx_immaterial" / "bundles" / "mermaid" /
              "mermaid.min.js")


def render_mermaid(page) -> int:
    """Transforme les blocs mermaid en schémas.

    Deux obstacles dans le builder `singlehtml` :
      1. le script mermaid n'est pas chargé (l'extension ne l'injecte que pour
         le builder `html`) ;
      2. le thème RETIRE la classe `mermaid` des <pre>, qui se retrouvent nus
         avec leur code source — d'où les diagrammes affichés en texte brut.

    On repère donc les blocs par leur PREMIER MOT (mot-clé mermaid), on leur
    remet la classe, puis on lance le rendu. Le compteur renvoyé permet de
    vérifier que ça a marché — sans lui, un échec passe inaperçu.
    """
    if not MERMAID_JS.exists():
        return 0
    tagged = page.evaluate("""() => {
        const KW = ['flowchart', 'graph', 'sequenceDiagram', 'classDiagram',
                    'stateDiagram', 'erDiagram', 'gantt', 'pie', 'journey'];
        let n = 0;
        for (const pre of document.querySelectorAll('pre')) {
            const txt = (pre.innerText || '').trim();
            const first = txt.split(/\s+/)[0];
            if (!KW.includes(first)) continue;      // bloc de code ordinaire
            pre.classList.add('mermaid');
            pre.textContent = txt;                  // mermaid veut le SOURCE brut
            n++;
        }
        return n;
    }""")
    if not tagged:
        return 0
    page.add_script_tag(content=MERMAID_JS.read_text(encoding="utf-8"))
    page.evaluate("""async () => {
        mermaid.initialize({startOnLoad: false, theme: 'neutral',
                            flowchart: {useMaxWidth: true}});
        await mermaid.run({querySelector: 'pre.mermaid'});
    }""")
    page.wait_for_timeout(2500)
    return page.evaluate(
        "() => document.querySelectorAll('pre.mermaid svg, .mermaid svg').length")


def to_pdf(html: Path, pdf: Path, title: str) -> None:
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(html.as_uri(), wait_until="networkidle")
        page.add_style_tag(content=PRINT_CSS)
        drawn = render_mermaid(page)
        print(f"     diagrammes rendus : {drawn}")
        pdf.parent.mkdir(parents=True, exist_ok=True)
        page.pdf(path=str(pdf), format="A4", print_background=True,
                 display_header_footer=True,
                 header_template=HEADER.format(title=title),
                 footer_template=FOOTER,
                 margin={"top": "18mm", "bottom": "20mm",
                         "left": "16mm", "right": "16mm"})
        browser.close()


def toc_pdf(body: Path, pdf: Path, title: str) -> None:
    """Construit la table des matières à partir des pages RÉELLES du corps.

    Les numéros ne peuvent pas être devinés : ils dépendent de la pagination
    de Chromium. On lit donc le PDF déjà produit et on repère la page où
    chaque titre de chapitre apparaît.
    """
    from pypdf import PdfReader
    from playwright.sync_api import sync_playwright

    reader = PdfReader(str(body))
    # Titres de chapitre = les <h1> du document, dans l'ordre.
    entries, seen = [], set()
    for num, pg in enumerate(reader.pages, start=1):
        for line in (pg.extract_text() or "").split("\n")[:3]:
            line = line.strip()
            if 6 < len(line) < 70 and line not in seen and line[0].isupper():
                seen.add(line)
                entries.append((line, num))
                break

    rows = "".join(
        f'<li><span>{label}</span><b>{num}</b></li>' for label, num in entries)
    html = f"""<style>
      @page {{ size: A4; margin: 20mm 22mm; }}
      body {{ font-family: "Segoe UI", Roboto, sans-serif; color: #1a1a2e; }}
      h1 {{ font-size: 22pt; margin: 0 0 8mm 0; }}
      ul {{ list-style: none; padding: 0; font-size: 10pt; }}
      li {{ display: flex; align-items: baseline; gap: 3mm; padding: 1.1mm 0;
            border-bottom: 1px dotted #ccc; }}
      li span {{ flex: 1; }}
      li b {{ font-variant-numeric: tabular-nums; color: #0F43FF; }}
    </style>
    <h1>Table des matières</h1><ul>{rows}</ul>"""

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_content(html, wait_until="load")
        page.pdf(path=str(pdf), format="A4", print_background=True)
        browser.close()
    print(f"     entrées de sommaire : {len(entries)}")


def cover_pdf(pdf: Path) -> None:
    """Imprime la couverture + la page légale dans un PDF à part."""
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto((ROOT / "_cover.html").as_uri(), wait_until="load")
        page.pdf(path=str(pdf), format="A4", print_background=True,
                 margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
        browser.close()


def merge(*parts) -> None:
    """merge(part1, part2, ..., destination)"""
    from pypdf import PdfWriter
    *sources, dest = parts
    w = PdfWriter()
    for src in sources:
        w.append(str(src))
    with open(dest, "wb") as fh:
        w.write(fh)


def main():
    wanted = sys.argv[1:] or list(LANGS)
    for lang in wanted:
        if lang not in LANGS:
            sys.exit(f"Langue inconnue : {lang} (attendu : {', '.join(LANGS)})")
        with tempfile.TemporaryDirectory() as tmp:
            html = build_singlehtml(lang, Path(tmp))
            body = Path(tmp) / "body.pdf"
            cover = Path(tmp) / "cover.pdf"
            toc = Path(tmp) / "toc.pdf"
            to_pdf(html, body, LANGS[lang])
            cover_pdf(cover)
            toc_pdf(body, toc, LANGS[lang])
            pdf = OUT / f"manuel-resthome-{lang}.pdf"
            pdf.parent.mkdir(parents=True, exist_ok=True)
            merge(cover, toc, body, pdf)
            print(f"  {pdf.relative_to(ROOT)}  "
                  f"({pdf.stat().st_size // 1024} Ko)")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
