# Dateinamen für Rätselhaft!

Unsere Buchdateien heißen `rk_<jahr>_<buch-id>.xml`, zum Beispiel `rk_1786_b0001.xml`.

- `rk`: Korpuskürzel.
- `jahr`: vier Ziffern oder `undatiert`.
- `buch-id`: `b` und vier Ziffern; stabile Buchkennung.
- `.xml`: einheitliche Dateiendung.

## Einheitlich und plattformverträglich

Für Buchdateien und Projektordner verwenden wir ASCII-Kleinschreibung, Ziffern, Unterstrich und Bindestrich. Keine Leerzeichen, Umlaute oder Doppelpunkte, keine reservierten Windows-Gerätenamen und keine nur durch Groß-/Kleinschreibung unterschiedenen Namen. Pfade bleiben kurz und relativ. Die etablierten Metadateien README.md, LICENSE, CITATION.cff und CHANGELOG.md behalten ihre Standardschreibweise.

Vollständiger Titel, Quelle und Datierung stehen in den TEI-Metadaten. Ein kurzer Dateiname ersetzt diese Beschreibung nicht. Die Jahresangabe im Namen wird bei der Aufnahme gegen die Metadaten geprüft. Für die Untersuchung werden Datenrelease und Auswahl festgehalten.

## Filtern mit Python

```python
from pathlib import Path
files = sorted(Path("data/tei").glob("rk_1786_*.xml"))
```

Damit lassen sich entsprechend benannte Bücher des Jahres 1786 auswählen. Undatierte Bücher werden mit `rk_undatiert_*.xml` ausgewählt.

## Änderungen und Prüfung

Die Regel wird vor der ersten Aufnahme in docs/dateinamen.md dokumentiert. Buchkennung bei Aufnahme vergeben und beibehalten. Bei korrigierter Datierung die Datei gezielt in Git umbenennen, Zuordnung und Grund im CHANGELOG festhalten. Andere Bezüge prüfen; Umbenennungen nicht beiläufig ausführen.

Namensmuster, Eindeutigkeit auch ohne Groß-/Kleinschreibung und doppelte Buchkennungen werden bei jedem Änderungsvorschlag geprüft. Der kleine Namensprüfer benötigt nur Python-Standardbibliothek:

```text
python dateinamen-pruefen.py data/tei
```

Er prüft Dateinamen, keine XML-Inhalte. Schema, Verweise, Metadaten und fachliche Qualität werden zusätzlich geprüft.
