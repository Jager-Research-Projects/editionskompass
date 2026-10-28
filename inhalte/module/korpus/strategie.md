# Git-Strategie für Rätselhaft!

Fiktives Projekt · Referenzpraxis 0.4.0

## Früh eine klare Publikation planen

Ein eigenes öffentliches Korpusrepo in einer GitHub-Projektorganisation enthält die freigegebenen Daten. Das Forschungsrepo bleibt für Quellen, Aufbereitung und eigene Studien zuständig.

## Einen maßgeblichen Bestand anbieten

data/tei enthält die Buchdateien nach einem dokumentierten Modell. README, Schema, Lizenz, Zitation und ein kleines Beispiel gehören dazu.

## Jede Änderung prüfen

Änderungen kommen über einen Pull Request. Automatische Prüfungen laufen bei jedem Vorschlag; eine zweite Person liest die betroffenen Stellen fachlich gegen.

## Geprüfte Releases veröffentlichen

Freigegebene Stände erhalten Tag, Release, Änderungsnotizen und ein unabhängiges Archivpaket mit Versionsnachweis.

## Lokale Forschung ermöglichen

Vollständige Downloads, kleine Einstiegsdaten, relative Pfade und dokumentierte Abhängigkeiten sind verbindlich. Eine API ist ein Zusatzangebot.

## Forschungsbezüge festhalten

Jede Untersuchung nennt Datenrelease, Auswahl, Extraktion und Skriptfassung. Ein Analysemanifest verbindet diese Angaben.

## Neue Annotation getrennt versionieren

Zusätzliche automatische Wortannotation wird zunächst als Stand-off-Schicht veröffentlicht. Sie nennt Basisrelease, Anker, Verfahren und Prüfstatus.

## Verantwortung nach Projektende benennen

Mindestens zwei autorisierte Zugangswege, eine gepflegte Anleitung und ein erreichbarer Kontakt sichern den Betrieb. Nach Förderende gilt begrenzte konservierende Pflege.

## Beispiele und Umsetzung

### Früh eine klare Publikation planen

**Beispiel:** Vor dem ersten Workshop stehen Zielgruppe, Datenumfang, Ordnerstruktur, Prüfung und Releaseweg im versionierten Publikationskonzept.

**Tipp:** Ein separates Publikationsrepo verhindert, dass interne Arbeitsstände beiläufig mitveröffentlicht werden.

### Einen maßgeblichen Bestand anbieten

**Beispiel:** Eine Nutzerin findet in README: „Für Analysen verwenden Sie data/tei dieses Releases. Beispiele stehen in examples/.“

**Tipp:** Nehmen Sie die Struktur als Ausgangspunkt. Eigene Ergänzungen bekommen eine erklärte Funktion.

### Jede Änderung prüfen

**Beispiel:** Ein Konverter ändert zehn Bücher: Schema und Verweise prüfen, Bestandsänderungen vergleichen und mindestens die betroffenen Strukturtypen gegenlesen.

**Tipp:** Ein laufendes Skript ist kein Qualitätsnachweis. Prüfumfang und fachliche Freigabe werden festgehalten.

### Geprüfte Releases veröffentlichen

**Beispiel:** v1.1 ergänzt Sammlungen und korrigiert Lösungen. CHANGELOG nennt die Änderungen; v1.0 bleibt als früherer Forschungsstand erhalten.

**Tipp:** Bereits veröffentlichte Fassungen nicht stillschweigend überschreiben. Fehler in einer neuen Version korrigieren.

### Lokale Forschung ermöglichen

**Beispiel:** Ein frisch entpacktes Beispiel liefert mit einem dokumentierten Aufruf das angegebene Ergebnis – ohne Uni-Konto oder Netzlaufwerk.

**Tipp:** Prüfen Sie den Einstieg auf einem anderen Rechner. Dokumentieren Sie die tatsächlich getestete Umgebung.

### Forschungsbezüge festhalten

**Beispiel:** Die Reimstudie verwendet Release v1.0, vier Rätselkennungen und den bezeichneten Export ohne Lösungen.

**Tipp:** Speichern Sie den Nachweis zusammen mit der Untersuchung, nicht nur als Link zum jeweils aktuellen Repo.

### Neue Annotation getrennt versionieren

**Beispiel:** Eine Wortartenannotation verweist auf v1.0 und die dortige Tokenisierung. Nutzende können Basisdaten ohne diese Schicht beziehen.

**Tipp:** Eine fachlich beschlossene Änderung am Basismodell ist möglich; sie erhält einen neuen Basisrelease. Zusätzliche Forschung bleibt zunächst getrennt.

### Verantwortung nach Projektende benennen

**Beispiel:** README nennt, wer wichtige Korrekturen prüft und dass neue Bücher nach verfügbarer Kapazität aufgenommen werden.

**Tipp:** Erproben Sie Nutzung und Releasevorbereitung vor dem Ausscheiden der Hauptbearbeiterin.
