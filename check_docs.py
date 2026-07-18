#!/usr/bin/env python3
"""check_docs.py — contrôle des conventions de contenu (inspiré d'un contrôle de conventions).

Vérifie chaque page de content/ :
  - un titre H1 unique en tête ;
  - un bloc :::{rh-description} (meta + JSON-LD) ;
  - aucun résidu MkDocs (admonitions !!!, grid cards, entités HTML échappées) ;
  - front-matter limité à howto_auto (title/description/faq passent par directives) ;
  - pas de lien ancré cross-fichier (page.md#ancre) — casse en i18n.

Usage :  python check_docs.py        (exit 1 si au moins une erreur)
"""
import re
import sys
import pathlib

CONTENT = pathlib.Path(__file__).resolve().parent / "content"
errors = []


def check(page, text):
    rel = page.relative_to(CONTENT).as_posix()
    lines = text.splitlines()

    # front-matter éventuel
    body = text
    if lines and lines[0].strip() == "---":
        end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
        if end:
            fm = "\n".join(lines[1:end])
            for k in ("title:", "description:", "faq:"):
                if re.search(rf"^{k}", fm, re.M):
                    errors.append(f"{rel}: `{k}` en front-matter → doit être un titre H1 / directive rh-*")
            body = "\n".join(lines[end + 1:])

    h1 = re.findall(r"^# .+", body, re.M)
    if len(h1) == 0:
        errors.append(f"{rel}: pas de titre H1 (`# …`)")
    elif len(h1) > 1:
        errors.append(f"{rel}: {len(h1)} titres H1 (un seul attendu)")

    if "{rh-description}" not in body:
        errors.append(f"{rel}: pas de bloc :::{{rh-description}} (meta/JSON-LD)")

    if re.search(r"^!!!\s", body, re.M):
        errors.append(f"{rel}: admonition MkDocs `!!!` non convertie (→ :::{{note}})")
    if 'class="grid cards"' in body:
        errors.append(f"{rel}: `grid cards` MkDocs non converti")
    if "&lt;!--" in body or "--&gt;" in body:
        errors.append(f"{rel}: entités HTML échappées (`&lt;!--` / `--&gt;`)")

    for m in re.finditer(r"\]\(([^)]+\.md)#([\w-]+)\)", body):
        errors.append(f"{rel}: lien ancré cross-fichier `{m.group(1)}#{m.group(2)}` "
                      f"→ casse en FR/NL (lier au niveau page)")


def main():
    pages = sorted(CONTENT.rglob("*.md"))
    for p in pages:
        check(p, p.read_text(encoding="utf-8"))
    print(f"check_docs : {len(pages)} pages contrôlées, {len(errors)} problème(s).")
    for e in errors:
        print("  [X]", e)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
