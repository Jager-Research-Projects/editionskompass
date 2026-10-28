# Rätselhaft! – Publikationskonzept 0.4

Die GitHub-Projektorganisation veröffentlicht das TEI-Korpus als wissenschaftliches Datenprodukt. Das Konzept wird von Beginn an versioniert und bei Änderungen fortgeschrieben.

## Für wen?

Studierende, Korpusforschende und Modellgruppen sollen selbstständig von einem Download zu einer nachvollziehbaren Untersuchung gelangen.

## Welcher Bestand?

data/tei enthält die maßgeblichen Buchdateien. Lösungen sind mit Rätselkennungen verbunden. Automatische Annotationen liegen getrennt und nennen Verfahren und Prüfstatus.

## Wie einsteigen?

README erklärt Bestand, Lizenz, Struktur und ersten Aufruf. Kleine Beispiele, Teilpakete und vollständige Daten sind ohne Uni-Konto lokal nutzbar.

## Wie freigeben?

Prüfungen, Bestandsvergleich und gezielte fachliche Lektüre gehen dem Release voraus. Tag, Releasenotizen und Archivpaket bezeichnen die Veröffentlichung.

## Wie verbessern?

Fehler werden als Issues gemeldet, Korrekturen geprüft und in neuen Releases beschrieben. Ältere Forschungsstände bleiben referenzierbar; ihre Mängel werden nicht zur Pflicht künftiger Fassungen.

## Struktur und Auszeichnung

data/tei enthält die maßgeblichen Buchdateien. Quellenkontext, Rätsel, Versgrenzen und Lösungen sind dokumentiert. Die Kennungen bleiben stabil; ein neues Modell oder eine Zusammenlegung bekommt eine Zuordnungstabelle. Unterschiedliche Auszeichnungspraktiken sind kenntlich. Zusätzliche automatische Annotationen benennen Verfahren, Werkzeugversion, Herkunft und Prüfstatus. Sie sind gezielt auswählbar und weglassbar.

README, LICENSE, CITATION.cff und CHANGELOG geben Einstieg, Nutzungsrechte, Zitation und Änderungen an. schema/ enthält das Modell, docs/ die Regeln, examples/ den kleinen Nutzungseinstieg und tests/ bekannte Prüffälle. Abgeleitete Exporte nennen Eingabe, Transformation und Fassung. Werkzeuge und zusätzliche Annotationen können getrennte Repos haben; konkrete Bezüge werden festgehalten.

## Technologie- und Infrastrukturoffenheit

Vollständige bezeichnete Downloads sind ohne Uni-Zugang nutzbar. Große Bestände werden zusätzlich sinnvoll portioniert; jede Paketaufteilung ist dokumentiert. Der erste Versuch benötigt kein riesiges Archiv. Offene Formate, relative Pfade und plattformverträgliche Dateinamen sind verbindlich. Getestete Umgebungen werden genannt. Das Python-Beispiel erleichtert den Einstieg, setzt aber Python nicht als einzigen Weg zur Verarbeitung der TEI-Daten voraus. Eine Bibliothek kann lokale Daten nutzen; die API ist ein Zusatzangebot.

## Prüfungen und Freigabe

Das Team prüft XML-Wohlgeformtheit, Schema, Kennungen und Verweise, unerwartete Bestandsänderungen, abgeleitete Ausgaben sowie ausgewählte Stellen gegen die Quelle. Eine erfolgreiche Analyse ersetzt keine Freigabe. Regressionstests sichern bekannte Konvertierungsfälle. Automatische Prüfungen und fachliche Kontrolle werden mit ihrem Umfang dokumentiert. Lea bereitet die Daten vor; Jonas prüft den technischen Ablauf; Miriam bestätigt die fachliche Freigabe.

## Fassungen, Fehler und Forschung

Freigegebene Stände bekommen Tags und Releases mit Bestand, Änderungen und bekannten Grenzen. Archivpakete erhalten passende Metadaten und einen Versionsbezug. Datenrelease, Auswahl, Extraktion und Werkzeugstand bilden zusammen den Forschungsnachweis. Bei Fehlern wird eine neue korrigierte Fassung veröffentlicht; betroffene alte Fassungen werden gekennzeichnet und bleiben referenzierbar. Eine mangelhafte Ordnerstruktur muss deshalb nicht fortgeführt werden.

## Beiträge und Pflege

README benennt Kontakt und Issue-Weg. Beiträge werden geprüft; Erweiterungen können als eigenständige versionierte Schichten verbunden bleiben. Nach Förderende gilt begrenzte konservierende Pflege. Aktive Erweiterungen benötigen Kapazität. Daten und Beispiele bleiben auch unabhängig von laufenden Diensten nutzbar.

## Vor jedem Release praktisch versuchen

Eine Person beginnt in einer frischen Umgebung beim Download, findet den maßgeblichen Bestand, führt das Beispiel aus und benennt Daten- und Verfahrensstand. Lücken fließen in README, Tests und Konzept ein.

## Benennung und Pflege

Buchdateien heißen rk_<jahr>_<buch-id>.xml. Die vollständige Namensregel steht in dateinamen.md. Das Repo-Handbuch repo-handbuch.md nennt für jeden Eintrag Zweck, Zielgruppe, Planung, Anlage, Mindestinhalt und Pflegeablauf.
