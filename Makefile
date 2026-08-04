# Resthome documentation — raccourcis de build et de prévisualisation.
#
# Tout passe par le venv du dépôt : aucune dépendance globale, et la même
# commande marche sous Git Bash, WSL et un shell POSIX.

PY  := .venv/Scripts/python.exe
# Sous Linux/macOS le venv range l'interpréteur ailleurs.
ifeq ($(wildcard $(PY)),)
PY  := .venv/bin/python
endif

PORT      ?= 8010
LIVE_PORT ?= 8000
LANG      ?= fr

.DEFAULT_GOAL := help
.PHONY: help build serve preview live check gettext pdf pdf-nl publish clean

help:
	@echo "Documentation Resthome"
	@echo ""
	@echo "  make serve       Construit le site puis le sert sur http://localhost:$(PORT)"
	@echo "                   (FR a la racine, /nl, /en — c'est le site REEL, traductions comprises)"
	@echo "  make preview     Sert le site DEJA construit, sans le reconstruire"
	@echo "  make live        Rechargement a chaud de la source EN sur http://localhost:$(LIVE_PORT)"
	@echo "                   (source anglaise uniquement — ne montre PAS les traductions)"
	@echo ""
	@echo "  make build       Construit ./site (les 3 langues) + statiques + sitemap"
	@echo "  make check       Controle les conventions de contenu"
	@echo "  make gettext     Re-extrait les POT et met a jour locale/{fr,nl}"
	@echo "  make pdf         Manuel PDF francais  (make pdf-nl pour le neerlandais)"
	@echo "  make publish     check + build + pdf — ce qu'il faut passer avant de committer"
	@echo "  make clean       Supprime ./site, ./_build et les PDF produits"
	@echo ""
	@echo "  Variables : PORT=$(PORT)  LIVE_PORT=$(LIVE_PORT)  LANG=$(LANG)"

build:
	$(PY) build_docs.py

# Le site construit est du HTML statique : un serveur de fichiers suffit, et
# `dirhtml` produit des dossiers avec index.html, que http.server sert bien.
preview:
	@test -d site || { echo "./site absent — lancez d'abord: make build"; exit 1; }
	@echo "-> http://localhost:$(PORT)/          (francais)"
	@echo "-> http://localhost:$(PORT)/nl/       (neerlandais)"
	@echo "-> http://localhost:$(PORT)/en/       (anglais)"
	$(PY) -m http.server $(PORT) --directory site

serve: build preview

# sphinx-autobuild rend la SOURCE (anglaise) et la recharge a chaud : pratique
# pour ecrire, inutile pour relire une traduction.
live:
	.venv/Scripts/sphinx-autobuild.exe -c . content _build/live -a 127.0.0.1:$(LIVE_PORT)

check:
	$(PY) check_docs.py

gettext:
	$(PY) build_docs.py --gettext

pdf:
	$(PY) build_pdf.py fr

pdf-nl:
	$(PY) build_pdf.py nl

publish: check build pdf

clean:
	rm -rf site _build _publish/manuel-resthome-*.pdf
