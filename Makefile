# Resthome documentation — raccourcis de build et de prévisualisation.
#
# PORTABILITÉ : sous Windows, `make` lance cmd.exe, qui n'a ni `test`, ni `rm`,
# ni accolades de regroupement, et dont le codepage n'est pas UTF-8. Aucune
# recette ci-dessous ne fait donc autre chose que LANCER UN PROGRAMME — toute
# la logique (garde, nettoyage, aide) vit dans docs-ops/mk.py, en Python.
#
# Tout passe par le venv du dépôt : aucune dépendance globale.

PY := .venv/Scripts/python.exe
# Sous Linux/macOS le venv range l'interpréteur ailleurs.
ifeq ($(wildcard $(PY)),)
PY := .venv/bin/python
endif
MK := $(PY) docs-ops/mk.py

# N'utilisez PAS le nom LANG : c'est une variable d'environnement standard
# (fr_FR.UTF-8 ici), et make ne l'écrase pas avec un ?=.
PORT      ?= 8010
LIVE_PORT ?= 8011

.DEFAULT_GOAL := help
.PHONY: help build serve preview live check gettext pdf pdf-nl publish clean

help:
	@$(MK) help --port $(PORT) --live-port $(LIVE_PORT)

build:
	$(PY) build_docs.py

# Le site construit est du HTML statique : un serveur de fichiers suffit, et
# `dirhtml` produit des dossiers avec index.html, que http.server sert bien.
preview:
	$(MK) preview --port $(PORT)

serve: build preview

# sphinx-autobuild rend la SOURCE (anglaise) et la recharge à chaud : pratique
# pour écrire, inutile pour relire une traduction.
live:
	$(MK) live --live-port $(LIVE_PORT)

check:
	$(PY) check_docs.py

gettext:
	$(PY) build_docs.py --gettext

pdf:
	$(PY) build_pdf.py fr

pdf-nl:
	$(PY) build_pdf.py nl

publish: check build pdf

# Ne touche pas aux PDF de _publish/ : ils sont versionnés (cf. mk.py).
clean:
	$(MK) clean
