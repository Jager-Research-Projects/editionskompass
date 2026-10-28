# Arbeitsordnung, Handbuch und Beteiligungsregeln

## Plausible erste Ordnerstruktur

```text
die-andere-stadt-edition/
├── README.md                 Einstieg und maßgebliche Daten
├── CITATION.cff              Angaben zur Zitation
├── LICENSE                  Nutzungsbedingungen des freigegebenen Bestands
├── CHANGELOG.md              Veröffentlichte Änderungen
├── CONTRIBUTING.md           Mitarbeit und Prüfung
├── MAINTAINERS.md            Aufgaben und Zuständigkeiten
├── data/
│   └── ms01/
│       └── eh-ms01-b012r.xml  Fachlich sinnvoll bearbeitbare Einheit
├── schema/                   ODD, Schema, zusätzliche Regeln
├── transforms/               Versionierte Überführung und Ableitungen
├── import/manifests/          Herkunft, Prüfsummen, Übernahmeprotokolle
├── docs/
│   ├── handbuch.md
│   ├── kennungen.md
│   ├── forschungsstaende.md
│   ├── publikationsstaende.md
│   └── uebergabe.md
└── tests/                    Technische und fachliche Prüffälle
```

Dies ist die vorgeschlagene Struktur des fiktiven Editionsrepos, nicht das Verzeichnis des Prototypen. Ganze Konvolute werden nur dann in eine Datei gelegt, wenn sie sinnvoll gemeinsam bearbeitet werden können. Der Pilot prüft Konflikthäufigkeit und Referenzen. Blattweise Dateien sind ein Beispiel; der tatsächliche Zuschnitt folgt dem Quellenzusammenhang.

Außerhalb liegen Frontendcode, autonome Forschungsrepos, die gesicherten Importpakete und die Bilddienste. Manifestdateien verbinden sie, ohne dieselben Bestände unkontrolliert zu vervielfältigen.

## Handbuch 1.0: verbindlicher Arbeitsablauf im Fall

1. Vor einer Bearbeitung den aktuellen Projektstand holen; bei offenen Konflikten Unterstützung anfordern.
2. Eine zusammengehörige Änderung bearbeiten und am Bild beziehungsweise an der fachlichen Grundlage prüfen.
3. Vergleich ansehen, passende Prüfung ausführen, Änderung mit Begründung sichern und übertragen.
4. Den vorgesehenen fachlichen Review auslösen. Ein automatischer Prüfstatus allein gibt keine Lesart frei.
5. Interne Rückfragen im vereinbarten Kanal bearbeiten; vertrauliche Inhalte und Zugangsdaten nicht in die Git-Geschichte aufnehmen.

## Handbuch 1.1: nach der Importprobe ergänzt

Nach abgenommenem Import ist die TEI-Datei im Editionsrepo die maßgebliche Arbeitsfassung dieser Einheit. Erneute Exporte ersetzen diese Datei nicht. Spätere Korrekturen werden verglichen, gezielt übernommen und geprüft. Das Übernahmeprotokoll nennt Herkunftsstand, Transformation, Abnahme und Kennungen. Die Produktionsphase endet nach Inventur und geregelter Übergabe verbleibender Einheiten.

## Beteiligungsregeln und Vereinbarungen

Vor dem Zugang werden Aufgabe, zulässige Datenverwendung, Lese-/Schreibbefugnisse, fachliche Freigabe, Beitragszuordnung und Schutzpflichten festgehalten. Interne Stände und Git-Geschichte dürfen nicht Unbefugten zugänglich gemacht werden. Lokale Kopien auf genutzten Geräten sind zu schützen. Möglicher unbefugter Zugriff, kompromittierte Zugangsdaten oder Verlust eines Geräts mit Projektkopien werden unverzüglich an Projektleitung und technischen Kontakt gemeldet.

Vor Ausscheiden oder Rollenwechsel wird vereinbart, welche Forschungsstände weiter genutzt und kopiert werden dürfen, welche Daten zurückzugeben oder zu löschen sind und welche dokumentierten Ausnahmen gelten. Assoziierte Weiterarbeit erhält eine passende neue Rolle. Eigene Forschungsrechte begründen keine automatische Freigabebefugnis für die offizielle Edition.

Das Projekt erfasst alle zugreifenden Parteien: Kernteam, Hilfskräfte, assoziierte Forschung, externe Technik, Verlag und Bibliothek. Personenbezogene Vereinbarungen, institutionelle Regelungen und Dienstleistungsvereinbarungen werden nach Aufgabe und Zugang zugeordnet. Git-Auswertungen erhalten einen transparent vereinbarten Zweck und Zugriffskreis; persönliche Leistungsranglisten gehören nicht zum Arbeitsablauf.

Die institutionelle Prüfung der später verwendeten Vereinbarung und ihrer rechtlichen Einbettung ist ein eigener Arbeitsschritt. Dieses Redaktionsdokument beschreibt den vorgesehenen Fall und liefert noch keine unterschriftsfertige Vertragsvorlage.
