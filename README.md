# Editionskompass

Deutsch-englische Orientierung zu Git für wissenschaftliche Editionsprojekte: vier Projektprototypen, vier Perspektiven, Lernangebote, Strategie- und Workshop-Planer sowie Materialien.

**Freigegebener Veröffentlichungsstand.** Website: https://jager-research-projects.github.io/editionskompass/ . Herausgeber und Redaktion: Thomas Jäger. Code: MIT; Texte und Lehrmaterialien: CC BY 4.0. Umfang und Medienrechte: RIGHTS.md.

## Bauen und prüfen

Python 3.12 und Node.js 22 bereitstellen:

```sh
python -m pip install -r requirements-lock.txt
npm ci
npx playwright install chromium
python scripts/build_pages.py
python tests/check_pages.py
npm test
```

`dist/` enthält den vollständigen statischen Portalstand und gemeinsam genutzte Webdateien. `inhalte/` und `scripts/` enthalten die zum Neubau benötigte Redaktion, eingefrorene Fallvorlagen, finale Übersetzungen und Bauprogramme. Interne Projektkonzepte, Rechercheunterlagen, Übersetzungsmodelle und die private Git-Historie gehören nicht zu diesem Repository.

`_site/` ist die fertige Pages-Ausgabe mit dem konfigurierten Projektpfad. Sie wird erzeugt und nicht in Git aufgenommen. Der Export passt auch interne PDF-Verweise an; Layout und Inhalt der PDFs bleiben erhalten. Ändern Sie Inhalte in den redaktionellen Quellen, nicht in `_site/`. Bereits erzeugte PDF-Materialien werden mitgeführt. Ihre redaktionelle Neuerzeugung ist ein gesonderter Schritt.

Lokale Vorschau: `python tests/serve_pages.py`, dann `http://127.0.0.1:8898/editionskompass/` öffnen. Der Testserver gibt absichtlich keine Dateien am Ursprungspfad `/assets/` frei. Damit werden fehlerhafte Pfade sichtbar.

GitHub Actions baut und prüft den Stand bei Änderungen und Pull Requests. Die Pages-Auslieferung erfolgt nur auf `main` und nach Freigabe in `publication.json`. Einzelheiten: DEPLOYMENT.md. Es werden keine GitHub-Zugangsdaten im Projekt benötigt.

## English

Editionskompass is a German–English guide to Git for scholarly editing, with four project cases, four perspectives, learning activities, strategy and workshop planners, and downloadable resources.

Public release of the complete German–English portal. Website: https://jager-research-projects.github.io/editionskompass/ . Publisher and editor: Thomas Jäger. Code: MIT; editorial and teaching content: CC BY 4.0 (see RIGHTS.md for scope and media provenance). The commands above rebuild and test the portal. `_site/` is generated; edit the editorial sources instead. Existing PDFs are included; the export adjusts their internal links without changing page content or layout.

No user-entered planner data are sent to a server. Browser storage, resource requests and GitHub hosting are explained in the website’s privacy information. AI-assisted drafting, translation, illustration and implementation are identified through the site’s provenance notices.
