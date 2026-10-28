# Empfehlung auf einen Blick
### So würden wir beginnen
Wir organisieren TEI-Dateien, Modell, Abfragen, Transformationen und Dokumentation als nachvollziehbaren Bestand in Git. XML-Werkzeuge ergänzen die Abfragefunktionen. Einen Datenbankdienst setzen wir ein, wenn er einen konkreten Nutzen bringt. Ein bereits betreuter institutioneller Dienst kann auch für ein kleines Projekt sinnvoll sein.
## Git und XML-Werkzeuge
Git ist der maßgebliche Bestand. Bearbeitende vergleichen und prüfen Änderungen, halten sie als Commit fest und übertragen sie in das gemeinsame Repository. XML-Werkzeuge lesen die Dateien. Die Veröffentlichung kann statisch erzeugt werden; auch eine laufende Anwendung ist möglich.
## Git führt, die Datenbank erschließt
Die maßgeblichen Editionsdaten liegen in Git. Ein geprüfter Import baut den Datenbankbestand auf. Die Datenbank bedient Abfragen und das Interface. Fachliche Korrekturen gehen über den vereinbarten Prüfweg zurück in Git; die Datenbank wird danach aktualisiert. Es gibt keine unkontrollierte zweite Schreibstelle.
## In der Datenbank bearbeiten, mit Git verbinden
Eine vorhandene DB-Oberfläche bleibt die maßgebliche Bearbeitungsumgebung. Ein definierter Export übergibt geprüfte Änderungen an Git. Dort werden die exportierten Daten und zugehörige Programme versioniert. Gleichzeitige Änderungen an exportierten Dateien und in der DB sind nicht ohne geregelte Rückführung zulässig.
Auch eine Datenbanklösung kann mit Versionierung eingerichtet werden. Eine zusammenhängende Geschichte der Änderungen an Texten, Schemata und Programmen entsteht dadurch jedoch nicht automatisch. Wir empfehlen, diese Geschichte mit Git zu erhalten und die Datenbank nach ihrem konkreten Nutzen einzusetzen.
## Was bleibt nach Projektende?
-
Editionsdaten
: TEI, Metadaten, Verknüpfungen, Modell, Dokumentation und Rechte.
-
Publikationsfassung
: Die konkrete Webausgabe, Register, Suchindex und gegebenenfalls Druck-/PDF-Ausgabe. Unverzichtbare externe Dienste benennen.
-
Herstellung und Prozessgeschichte
: Relevante Git-Historie, Abfragen, Transformationen, Tests, Konfigurationen, Abhängigkeiten und Entscheidungsnotizen.
Statisch oder dynamisch ist eine eigene Entscheidung. Git kann eine laufende Anwendung versorgen; eine Datenbank kann statische Ausgaben erzeugen. Ein Git-Repository ersetzt weder einen Archivdienst noch die Finanzierung eines laufenden Systems.
Redaktionelle Grundlage: die beiden bereitgestellten Arbeitsdokumente zu Git und XML-Datenbanken. Text, Übersetzung, schematische Grafiken und Umsetzung wurden KI-unterstützt erstellt. Version 1.0 · 28.10.2026. Die Grafiken zeigen Arbeitsmodelle, keine reale Installation.
