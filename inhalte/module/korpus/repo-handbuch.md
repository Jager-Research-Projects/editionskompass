# Rätselhaft! – Aufbau und Pflege des Publikationsrepos

Muster für das Projekt · 22. Oktober 2026. Die Vorschauen sind Ausschnitte, die den jeweiligen Inhalt und Prozess erläutern.

## README.md

Die Eingangstür: Was ist das Korpus und wie beginne ich eine Untersuchung?

### Für wen und in welchem Ton?

Neue Nutzende, Studierende und Forschende. Kurz, einladend und handlungsorientiert schreiben; Fachbegriffe erklären, auf Details verlinken.

### Wann planen?

Mit dem Publikationskonzept. Die erste Aufgabe einer neuen Nutzerin festlegen.

### Wann anlegen?

Bei Einrichtung des Publikationsrepos, vor dem ersten Datenrelease.

### Wann und wie aktualisieren?

Bei jeder Änderung an Einstieg, Ordnern, Aufrufen, Lizenz, Zitierweise oder Kontakt im selben Pull Request mitändern. Vor jedem Release den Einstieg von einer anderen Person ausführen lassen.

### Was lässt sich automatisieren?

Relative Links und Beispielaufruf automatisch prüfen. Eine Textänderung wird fachlich gegengelesen; README wird nicht allein aus Commitnachrichten erzeugt.

### Mindestinhalt

- Zweck und Umfang des Korpus
- Maßgeblicher Datenordner und aktuelle Releases
- Erster Download, Aufruf und erwartetes Ergebnis
- Links zu Auszeichnung, Lizenz und Zitation
- Kontakt, Beiträge und Pflegezusage

### Beispielausschnitt

```text
# Rätselhaft! – TEI-Korpus

Für Korpusanalysen verwenden Sie data/tei dieses Releases.
Eine XML-Datei entspricht einem Buch oder einer Sammlung.

## Erste Untersuchung
Kleines Beispiel: examples/nutzungsstart/
Aufruf: python examples/nutzungsstart/untersuchen.py
Erwartet: drei Rätsel und drei zugeordnete Lösungen.

Auszeichnung: docs/auszeichnung.md
Dateinamen: docs/dateinamen.md
Zitation: CITATION.cff · Nutzungsrechte: LICENSE
Fehler mit Release und Rätselkennung als Issue melden.
Nach Projektende: wichtige Korrekturen, neue Aufnahmen nach Kapazität.
```

## LICENSE

Legt nachvollziehbar fest, unter welchen Bedingungen die Bestandteile nachgenutzt werden dürfen.

### Für wen und in welchem Ton?

Alle Nachnutzenden. Lizenztexte unverändert übernehmen; Geltungsbereich daneben klar und ohne eigene juristische Umschreibungen erklären.

### Wann planen?

Bei der Quellenauswahl: Nutzungsbedingungen erfassen und klären, welche Lizenz für welche Projektbestandteile gilt.

### Wann anlegen?

Vor der ersten öffentlichen Freigabe nach abgeschlossener Rechteklärung.

### Wann und wie aktualisieren?

Bei neuen Quellen oder anders lizenzierten Bestandteilen den Geltungsbereich prüfen. Änderungen fachlich freigeben und in den Releasenotizen erklären; bestehende Lizenztexte nicht beiläufig austauschen.

### Was lässt sich automatisieren?

Eine Prüfung kontrolliert, ob LICENSE vorhanden ist und neue Quellen Rechteangaben haben. Die Entscheidung über Nutzungsrechte wird nicht automatisiert.

### Mindestinhalt

- Bezeichnung und vollständiger Text der gewählten Lizenz
- Eindeutiger Geltungsbereich für Daten, Dokumentation und Code
- Quellen-/Rechtehinweise und kenntliche Ausnahmen
- Verweise aus README und Quelldokumentation

### Beispielausschnitt

```text
Aufbau der Datei nach Rechteklärung:

1. Geltungsbereich: Welche Daten oder Werkzeuge?
2. Name und vollständiger Originaltext der gewählten Lizenz
3. Verweis auf Quellen-/Rechtehinweise

Unterschiedliche Lizenzen für Daten und Code werden ausdrücklich
getrennt zugeordnet. Eine Liste von Lizenznamen allein reicht nicht.
```

## CITATION.cff

Bietet strukturierte Angaben zum Zitieren der Datenpublikation.

### Für wen und in welchem Ton?

Forschende und Zitationswerkzeuge. Präzise bibliografische Metadaten; keine Werbesprache. Ein kurzer Zitierhinweis in README ergänzt die Datei.

### Wann planen?

Mit dem Publikationskonzept: Titel, Verantwortliche und Versionsbezug festlegen.

### Wann anlegen?

Vor dem ersten Release anlegen und mit einem CFF-Prüfwerkzeug validieren.

### Wann und wie aktualisieren?

Bei jedem Release Version und Datum aktualisieren; den bestätigten Versionsidentifikator nach der Archivierung eintragen. Autorenschaften bei relevanten Beiträgen prüfen. Alle Metadaten im Releaseablauf abgleichen.

### Was lässt sich automatisieren?

CFF-Syntax und erforderliche Angaben prüfen. Titel, Version und Datum können aus einer gemeinsamen Releasequelle vorbelegt werden; Autorenschaft und Archivnachweis bewusst bestätigen.

### Mindestinhalt

- CFF-Version und Nachricht zum Zitieren
- Titel und Ressourcentyp
- Verantwortliche mit Namen, gegebenenfalls ORCID
- Datenversion und Veröffentlichungsdatum
- Bestätigte Identifikatoren und Bezugsadresse

### Beispielausschnitt

```text
cff-version: 1.2.0
message: "Bitte zitieren Sie die verwendete Datenversion."
type: dataset
title: "Rätselhaft! – TEI-Korpus"
authors:
  - family-names: Berger
    given-names: Lea
version: 1.0.0
date-released: 2026-10-22
# Weitere Verantwortliche und bestätigten Versionsnachweis ergänzen.
# Versions-DOI nach bestätigter Archivierung eintragen.
```

## CHANGELOG.md

Erklärt, was sich für Nutzende zwischen zwei Datenfassungen geändert hat.

### Für wen und in welchem Ton?

Forschende, die Ergebnisse wiederholen oder einen neuen Release verwenden. Bestands- und Bedeutungsänderungen benennen; keine ungefilterte Commitliste.

### Wann planen?

Zusammen mit Versionsschema und Releaseweg.

### Wann anlegen?

Mit der ersten öffentlichen Version. Laufende Änderungen zunächst unter „Unveröffentlicht“ sammeln.

### Wann und wie aktualisieren?

Jeder Pull Request mit nutzbarer Daten-/Modelländerung ergänzt einen Eintrag. Vor dem Release Einträge ordnen, Datum und Version setzen; bekannte Fehler betroffener älterer Fassungen kennzeichnen.

### Was lässt sich automatisieren?

Vorlagen und aus Pull Requests gesammelte Notizen sparen Arbeit. Die Redaktion prüft ihre wissenschaftliche Aussage; eine rohe Git-Log-Ausgabe ist kein Changelog.

### Mindestinhalt

- Version und Datum
- Neu aufgenommene oder entfernte Bestände
- Korrekturen und betroffene Kennungen
- Modell-/Auszeichnungsänderungen mit Auswirkungen
- Bekannte Grenzen und gegebenenfalls Migrationshinweise

### Beispielausschnitt

```text
# Änderungen

## Unveröffentlicht
- Reimannotation wird als zusätzliche Schicht vorbereitet.

## 1.1.0 – Beispielrelease
- Ergänzt: neue Sammlung b0003.
- Korrigiert: Lösungszuordnungen in b0001, IDs unverändert.
- Auswirkung: Auswertungen mit Lösungen bitte erneut prüfen.

## 1.0.0 – Erster geprüfter Bestand
- Umfang und bekannte Grenzen im Release beschrieben.
```

## data/

Enthält den maßgeblichen veröffentlichten Datenbestand; Rohübernahmen und Studienkopien gehören nicht als konkurrierende Fassungen daneben.

### Für wen und in welchem Ton?

Menschen und Programme. Vorhersehbare Struktur und maschinenlesbare Metadaten; erläuternde Prosa in README oder docs.

### Wann planen?

Vor der Aufnahme der ersten Buchdateien: Einheit, Kennungen, Metadaten und Paketaufteilung festlegen.

### Wann anlegen?

Mit dem ersten geprüften Teilbestand.

### Wann und wie aktualisieren?

Neue oder korrigierte Daten über Pull Requests prüfen und fachlich freigeben. Erst ein Release macht den geprüften Gesamtstand zur bezeichneten Forschungsgrundlage.

### Was lässt sich automatisieren?

Namensmuster, ID-Eindeutigkeit, XML/Schema, Verweise und Bestand prüfen. Fachliche Aufnahme und Freigabe bleiben ein eigener Schritt.

### Mindestinhalt

- Eindeutiger Korpusordner tei/
- Eine Buch-/Sammlungsdatei pro Einheit
- Dokumentierte IDs, Herkunft und Datierung
- Keine beiläufigen Exporte oder privaten Arbeitskopien

### Beispielausschnitt

```text
data/
└── tei/
    ├── rk_1786_b0001.xml
    ├── rk_1820_b0003.xml
    └── rk_undatiert_b0004.xml

Jede Kennung gehört zu genau einer Buch-/Sammlungsdatei.
Für Studien werden Releases und Auswahlregeln festgehalten.
```

## data/tei/

Hält die Buchdateien in derselben dokumentierten TEI-Auszeichnung bereit.

### Für wen und in welchem Ton?

Korpusforschende und Programme. Gleiche Strukturen bedeuten im ganzen Bestand dasselbe; automatische Zusatzannotation wird getrennt angeboten.

### Wann planen?

Einheit und TEI-Modell vor den ersten größeren Konvertierungen festlegen.

### Wann anlegen?

Für die erste geprüfte Buchdatei; Grenzfälle sofort dokumentieren.

### Wann und wie aktualisieren?

Bei Konvertierungen vor/nachher Bestand vergleichen. Modelländerungen zusammen mit Schema, Dokumentation und Migrationshinweis versionieren.

### Was lässt sich automatisieren?

Schema und Verweise bei Änderungen prüfen. Jahresangabe und Buchkennung im Dateinamen gegen die maßgeblichen Metadaten prüfen.

### Mindestinhalt

- Quellenbeschreibung und Buchkennung
- Rätselkennungen und Vers-/Textstruktur
- Lösungen mit eindeutiger Zuordnung
- Explizite Kennzeichnung von Unsicherheiten
- Einheitliches Dateinamensmuster

### Beispielausschnitt

```text
rk_1786_b0001.xml
rk_1820_b0003.xml
rk_undatiert_b0004.xml

Schnellauswahl der Beispieldatierung 1786:
data/tei/rk_1786_*.xml

Auswahl für die Untersuchung zusammen mit dem Release dokumentieren.
```

## rk_1786_b0001.xml

Eine vollständige Buch- oder Sammlungsdatei; Dateiname und stabile Kennung verbinden Ablage und Metadaten.

### Für wen und in welchem Ton?

Fachlich Lesende und automatisierte Verfahren. TEI-Struktur folgt dem Modell; Unsicherheiten in den Metadaten klar benennen.

### Wann planen?

Kennung bei der Aufnahme vergeben. Namensregel gilt schon bei der ersten Datei.

### Wann anlegen?

Nach Erfassung der Quelle und Zuordnung der Buchkennung.

### Wann und wie aktualisieren?

Korrekturen im selben Dateipfad nachvollziehbar committen. Ändert sich die Datierung, gezielt umbenennen und Zuordnung im Changelog erklären; die stabile Buchkennung bleibt erhalten.

### Was lässt sich automatisieren?

Ein Namensprüfer kann Regelverstöße und doppelte Buchkennungen finden. Änderungen an Titel oder Interpretation brauchen nicht ständig neue Dateinamen.

### Mindestinhalt

- Korpuskürzel rk
- Vierstellige Jahresangabe oder undatiert
- Stabile Buchkennung b0001
- Dateiendung .xml
- Übereinstimmung mit dokumentierten Metadaten

### Beispielausschnitt

```text
rk_1786_b0001.xml
│  │    └── stabile Buchkennung
│  └─────── dokumentiertes Erscheinungsjahr
└────────── Korpuskürzel

Metadaten enthalten den vollständigen Titel, Quelle und Datierung.
Der Dateiname ist ein kurzer, einheitlicher Einstieg für Filter.
```

## schema/

Veröffentlicht die Regeln, nach denen der Korpusbestand technisch geprüft wird.

### Für wen und in welchem Ton?

Bearbeitende und technische Nachnutzende. Regeln mit kleinen Grenzfallbeispielen erklären; Fachbedeutung in docs beschreiben.

### Wann planen?

Mit dem TEI-Modell und vor einer großen automatisierten Aufnahme.

### Wann anlegen?

Sobald das erste Datenmodell geprüft werden kann.

### Wann und wie aktualisieren?

Jede Modelländerung ändert Schema, betroffene Daten, Tests und Dokumentation im selben Änderungsvorschlag. Schemafassung im Release festhalten.

### Was lässt sich automatisieren?

Schemaerzeugung und Datenvalidierung sind automatisierbar. Tests müssen sowohl gültige als auch bewusst ungültige Fälle prüfen.

### Mindestinhalt

- Projektanpassung des TEI-Modells
- Ausführbares Schema und weitere Prüfregeln
- Anleitung zur Erzeugung und Ausführung
- Verbindung zur Auszeichnungsdokumentation

### Beispielausschnitt

```text
schema/
├── korpus.odd
├── korpus.rng
└── README.md

ODD: dokumentierte TEI-Anpassung.
RNG: daraus erzeugte Strukturprüfung.
README: Erzeugung, Abhängigkeiten und Prüfaufruf.
```

## docs/

Hält die verbindlichen Projektregeln und erläutert fachliche Entscheidungen.

### Für wen und in welchem Ton?

Neue Mitwirkende und externe Forschende. Begriffe erklären, Regeln knapp formulieren und mit korrekten Beispielen belegen.

### Wann planen?

In der Konzeptphase Gliederung und Verantwortung für Regeln festlegen.

### Wann anlegen?

Mit dem ersten Modell und den ersten Arbeitsregeln; nicht erst am Projektende nachschreiben.

### Wann und wie aktualisieren?

Bei geänderten Regeln zusammen mit Daten, Schema oder Werkzeugen anpassen. Fachliche Entscheidungen aus Issues in die dauerhafte Dokumentation übernehmen. Vor Releases Widersprüche prüfen.

### Was lässt sich automatisieren?

Links und Beispiele prüfen; ein Pull-Request-Formular fragt nach betroffenen Dokumentationsstellen. Inhalte werden fachlich gegengelesen.

### Mindestinhalt

- Publikationskonzept und Korpusumfang
- TEI-Auszeichnung mit Beispielen
- IDs, Dateinamen und Metadaten
- Prüf-/Freigabe- und Releaseablauf
- Kontakt, Beiträge und Pflegeumfang

### Beispielausschnitt

```text
docs/
├── publikationskonzept.md
├── auszeichnung.md
├── dateinamen.md
└── releaseablauf.md

Aus dateinamen.md:
Eine Buchdatei heißt rk_<jahr>_<buch-id>.xml.
Jahr: vier Ziffern oder undatiert. Buch-ID: b plus vier Ziffern.
Die Zuordnung wird bei Aufnahme und Release geprüft.
```

## examples/

Ermöglicht eine kleine vollständige Untersuchung ohne persönliche Einführung.

### Für wen und in welchem Ton?

Neue Nutzende, Lehrveranstaltungen und Anschlussprojekte. Schrittweise Anleitung, wenige Abhängigkeiten und erwartete Ausgabe statt bloßer Skriptsammlung.

### Wann planen?

Mit dem ersten Nutzungsszenario: Welche Aufgabe soll jemand in wenigen Schritten schaffen?

### Wann anlegen?

Vor dem ersten öffentlichen Release mit einem kleinen passenden Datenausschnitt.

### Wann und wie aktualisieren?

Wenn Datenmodell, Aufruf oder Abhängigkeiten wechseln, Beispiel und Anleitung im selben Pull Request anpassen. Vor jedem Release frisch ausführen; gelegentlich von einer neuen Person ausprobieren lassen.

### Was lässt sich automatisieren?

Das Beispiel in einer frischen Umgebung ausführen und Ergebnis vergleichen. Ein zusätzlicher menschlicher Einstiegstest prüft die Verständlichkeit.

### Mindestinhalt

- Kleine vollständig nutzbare Beispieldaten
- Kurze Anleitung mit Aufruf
- Skript/Notebook samt Abhängigkeiten
- Erwartete Ausgabe
- Daten- und Werkzeugbezüge

### Beispielausschnitt

```text
examples/
└── nutzungsstart/
    ├── README.md
    ├── korpus.xml
    ├── untersuchen.py
    └── ausgabe/
        └── ergebnis.json

Aufruf aus dem Repository-Hauptordner:
python examples/nutzungsstart/untersuchen.py
Erwartet: 3 Rätsel, 3 Lösungen und getrennte Exporte.
```

## tests/

Macht bekannte Fehler automatisch wiedererkennbar und beschreibt den Prüfumfang.

### Für wen und in welchem Ton?

Bearbeitende und technische Verantwortliche. Prüffälle mit Erwartung und fachlichem Grund benennen; kleine überschaubare Testdaten verwenden.

### Wann planen?

Zusammen mit Konvertierung und Modell: Was darf ein Verarbeitungsschritt nicht verlieren?

### Wann anlegen?

Beim ersten Import und beim ersten Werkzeug. Jeder gefundene Fehler ergänzt einen Prüffall.

### Wann und wie aktualisieren?

Bei Daten-/Modell-/Werkzeugänderungen Erwartungen fachlich prüfen. Einen fehlschlagenden Test nicht nur passend umschreiben; Ursache klären. Vor dem Release vollständigen Prüflauf ausführen.

### Was lässt sich automatisieren?

Bei jedem Pull Request automatisiert ausführen. Der Bericht nennt geprüfte Eigenschaften; die fachliche Quellenkontrolle und Freigabe werden zusätzlich festgehalten.

### Mindestinhalt

- Prüfaufruf und Abhängigkeiten
- Gültige und gezielt ungültige Fälle
- IDs, Verweise und Inhaltserhalt
- Dateinamen-/Metadatenprüfung
- Regressionstests für bekannte Fehler

### Beispielausschnitt

```text
tests/
├── README.md
├── pruefe_dateinamen.py
├── pruefe_verweise.py
└── fixtures/
    ├── mit-loesungen.xml
    └── ohne-loesungen-fehler.xml

Erwartung: zwei Rätsel UND zwei zugeordnete Lösungen.
Ein reiner XML-Test würde den Verlust nicht erkennen.
```
