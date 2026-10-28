# Git-Handbuch der Albrecht-Edition

Fiktives Albrecht-Projekt · eigenständiges Musterdokument

**Fassung:** 1.1 · **Status:** Freigegebene Projektregelung · 21. Oktober 2026

**Verantwortlich:** Samir Demir · wissenschaftlich-technische Redaktion

**Freigabe:** Nora Seidel für die Fachredaktionen · Eva Brandt für die Gesamtkoordination

**Nächste Prüfung:** 21. April 2027

Dieses Handbuch gilt für alle Arbeitsgruppen der Albrecht-Edition. Es beschreibt die verbindliche gemeinsame Praxis und kennzeichnet Empfehlungen ausdrücklich. Die jeweils gültige Fassung liegt im geschützten Repository standards unter governance/git-handbuch.md. Neue Mitarbeitende erhalten eine Einführung vor dem ersten produktiven Commit.

## 0. Soforthilfe: nichts überstürzt überschreiben

H00 · Regel

Bei unklarem Stand: Arbeit sichern, git status und git diff ansehen und die wissenschaftlich-technische Redaktion ansprechen. Keine unklaren Konflikte durch blindes Übernehmen einer Seite lösen. Bei versehentlich eingebrachten Geheimnissen oder vertraulichen Angaben sofort IT und Redaktion verständigen – auch wenn die aktuelle Datei schon korrigiert wurde.

Niemand schreibt geteilte oder archivierte Historien eigenmächtig um. Die Redaktion koordiniert notwendige Eingriffe mit IT und den zuständigen Stellen. Kompromittierte Zugangsdaten werden gesperrt; eine Dateilöschung allein genügt nicht.

## 1. Geltung und Pflege

H01 · Regel

Die Arbeitsgruppen pflegen Texte in Bereichsrepos. Das gemeinsame Standards-Repo enthält Handbuch, Editionsrichtlinien, Schema/ODD, Prüfregeln, Profil- und Transformationsdokumentation. Das zentrale Register wird in der Registerdatenbank gepflegt. Seine freigegebenen Snapshots werden eindeutig mit den Textständen verbunden.

Samir betreut das Handbuch gemeinsam mit einer benannten technischen Vertretung. Fachredaktionen prüfen fachliche Regeln; Eva sichert Mandat und Pflegezeit. Zum 21. April und 21. Oktober wird das Handbuch durchgesehen, außerdem nach Vorfällen sowie Modell- und Werkzeugwechseln.

Änderungsvorschläge erhalten ein GOV-Ticket mit Anlass, betroffenen Abschnitten und Geltungsbereich. Fachliches und technisches Review gehen der Freigabe voraus. Die freigegebene Fassung wird getaggt, im Team erläutert und schriftlich angekündigt. Frühere Fassungen bleiben intern erreichbar. Das Handbuch erweitert keine Rechte oder Analysezwecke der Mitarbeitervereinbarung.

## 2. Zuständigkeit und Zuschreibung

H02 · Regel

Jeder Auftrag benennt Ausführung, wissenschaftliche Verantwortung und fachliche Prüfung. Eine Hilfskraft kann eine von Nora verantwortete Entscheidung umsetzen; ihre technische Bearbeitung und Noras wissenschaftliche Verantwortung werden getrennt dokumentiert. Neue Lesarten oder unklare Zuordnungen werden fachlich entschieden, bevor sie als gesicherter Befund übernommen werden.

Persönliche Git-Kennungen wie alb-k7m42 bleiben stabil und werden nicht wiedervergeben. Autor- und Committer-Felder führen diese Kennungen mit einer technischen Projektadresse. Das getrennte institutionelle Identitätsregister verwaltet die Zuordnung. Bots haben eigene Kennungen. Wissenschaftliche Beiträge und Verantwortung werden namentlich in TEI-Metadaten und Beitragsnachweisen ausgewiesen. Diese Angaben können Rückschlüsse erlauben; pseudonyme Historien bleiben geschützt.

## 3. Geräte und Zugänge

H03 · Regel

Arbeitsrepos werden ausschließlich auf institutionell verwalteten, verschlüsselten Geräten oder in der bereitgestellten Remote-Arbeitsumgebung geöffnet. Das gilt auch für externe Mitwirkende. Anmeldung erfolgt personenbezogen mit Mehrfaktorauthentifizierung; Schlüssel und Tokens werden nicht geteilt.

Private Git-Accounts, öffentliche Forks, persönliche Clouds und unregistrierte Spiegelungen sind für interne Bestände ausgeschlossen. IT führt das Geräte- und Berechtigungsverzeichnis. Der Entzug eines Serverzugangs löscht lokale Klone nicht; ihre Behandlung gehört zur dokumentierten Übergabe.

Vor dem Zugriff wird die Person im Beteiligungs- und Zugangsverzeichnis der passenden Aufgabe zugeordnet. Einführung, Vereinbarung, Gerätefreigabe und Berechtigungen werden bestätigt. Eine technische Git-Schulung einschließlich des eingesetzten oXygen-Git-Clients gehört dazu.

## 4. Der tägliche Arbeitsweg

H04 · Regel

Vor Beginn richtigen Arbeitsbereich, Branch und offenen Dateistand prüfen; den freigegebenen Stand abrufen und nach Projektverfahren abgleichen. Jede Aufgabe erhält ein ED-, DATA- oder BUG-Ticket. Kurze Arbeitszweige heißen beispielsweise ed/ED-142-registerbezug oder fix/BUG-58-zeitraum.

Vor dem Commit: Diff lesen, betroffene TEI-Dateien validieren, Dateimenge und vertrauliche Inhalte prüfen. Ein Commit enthält eine zusammenhängende prüfbare Änderung. Textkorrektur und globale Formatumstellung werden getrennt. Die Commitnachricht nennt Tätigkeit, Objekt, konkrete Änderung und Ticket, etwa: reg(Brief-017): Empfängerbezug berichtigen [ED-142].

Ein Merge Request bündelt Ziel, Ticket, fachliche Begründung, Prüfungen und offene Fragen. main ist geschützt. Inhaltliche Änderungen brauchen eine fachlich zuständige zweite Person; Änderungen an Modell, Schnittstelle oder Prüfablauf zusätzlich die technische Redaktion. Übernahme erfolgt mit Merge Commit. Abweichungen bedürfen einer dokumentierten Freigabe; bereits geteilte Beiträge werden nicht heimlich umgeschrieben.

## 5. TEI und oXygen

H05 · Regel

Die Redaktion verteilt das freigegebene oXygen-Projektprofil mit zugeordnetem Schema und dokumentierter Programmversion. Author Mode dient der regulären Bearbeitung; Text Mode der gezielten XML-Kontrolle. Nach beiden wird der Diff geprüft.

Bestehende Zeichen, Abstände, Einrückung und Zeilenenden bleiben erhalten, soweit die Aufgabe keine Änderung verlangt. Automatische Komplettformatierung und harte automatische Zeilenumbrüche sind für Editionsdateien deaktiviert. Visueller weicher Umbruch bleibt erlaubt. Profilwechsel werden an repräsentativen Dateien durch Öffnen, kleine Änderung, Speichern und Diff getestet.

Eine unbeabsichtigt neu formatierte Datei wird nicht pauschal übernommen. Gewollte Arbeit zunächst sichern und die Wiederherstellung mit der Redaktion abstimmen. Geplante Formatmigrationen erhalten einen isolierten Auftrag. Ein grüner Schematest ersetzt weder die Kontrolle der Zeichen noch die wissenschaftliche Prüfung.

## 6. Übergangsregel: nach dem Registerabgleich erneut prüfen

H06 · Regel

Nach dem Rückimport aus der Kommentaroberfläche werden die veränderten Kommentare gezielt auf erhaltene Striche, geschützte Abstände und Datumsannotation geprüft. Ein Zeitraum wie 1848–1849 muss als zusammengehörender Zeitraum erhalten bleiben. Die automatisch erzeugte Annotationsschicht für das Register wird vor der Freigabe kontrolliert.

Der Regressionstest enthält Bereichsstrich, geschützten Abstand, Zeitraumauszeichnung und eine sachliche Kommentarkorrektur ohne Änderung der Zeitangabe. Er prüft den gesamten Hin-und-zurück-Weg. Nora bestätigt die fachliche Erwartung; Samir verantwortet den Test.

Korrekturen gehen in den maßgeblichen Bestand zurück. Register-Snapshot, Satz, Web-Findemittel und betroffene Registerausgaben werden aus dem abgestimmten Stand neu abgeleitet und geprüft. Auch eine später rein sachliche Korrektur durchläuft diese Kontrolle. Stille Reparaturen ausschließlich in der Fahne sind keine abgeschlossene Korrektur.

H06 sichert die Zeit bis zur fachlich-technischen Abnahme des überarbeiteten Kommentartools ab. Die Tooländerung hat einen eigenen Auftrag und Regressionstest. Nach ihrer Bewährung wird die Notwendigkeit der Zusatzkontrolle neu bewertet und das Handbuch erneut angepasst.

## 7. Prüfungen und fachliche Freigabe

H07 · Regel

Vor jeder Integration laufen XML-Wohlgeformtheit, projektspezifisches Schema, zusätzliche Referenz-/Konsistenzregeln, Git-Kennungsprüfung und Sicherheitsprüfungen. Formatierungswarnungen werden geklärt. Die prüfende Person hält fest, was sie fachlich geprüft hat: Quelle, Identifikation, Interpretation oder Nebenwirkungen.

Ein technischer Prüferfolg erteilt keine wissenschaftliche oder rechtliche Freigabe. Blockierende Schutzprüfungen werden nicht routinemäßig übergangen. Notwendige Ausnahmen werden mit Begründung und zuständiger Freigabe dokumentiert.

## 8. Neue Werkzeuge und Altdaten

H08 · Regel

Neue Verfahren werden auf einem getrennten Testbestand erprobt. Der Auftrag dokumentiert Eingabe, Regel-/Programmversion, erwartete Ergebnisse, Rechte, Datenübertragung, Fehlerfälle und Rücknahmeweg. Das gilt auch für OCR und LLM. Geschützte Daten gehen nicht ohne Freigabe an externe Dienste.

Editorisch relevante Vorschläge werden vor der Übernahme fachlich geprüft. Bei geeigneten beaufsichtigten Verfahren bleiben Kontrolle und Rücknahme wirksam. Für Altdaten wird festgehalten, welche Bestände mit welcher Regelversion nachgezogen und welche Ausnahmen fachlich geprüft wurden. Neue Regeln gelten nicht stillschweigend als Maßstab früherer Arbeit.

## 9. Integration, Publikation und Rechte

H09 · Regel

Die Integration übernimmt geprüfte Datenpakete und ein internes Importmanifest mit Quellrepo, Quellcommit, Register-Snapshot, Prüfung und Rechtevermerk. Vollständige Arbeitsgeschichten bleiben in den geschützten Herkunftsrepos. Ein Datenpaket und eine Git-Historie sind verschiedene Übergabegegenstände.

Die Publikationsumgebung erzeugt aus freigegebenen Quellen einen eigenen öffentlichen Bestand mit eigener Geschichte. Sie übernimmt keine internen Commits. Nora verantwortet die wissenschaftliche Paketfreigabe; die Rechte-/Publikationsstelle prüft Materialrechte und Verlagsbedingungen. Clara wird in die vereinbarten Produktionsübergaben einbezogen.

Vor Veröffentlichung werden Daten, Metadaten, XML-Kommentare, Bilder, erzeugte Dateien sowie alle öffentlich erreichbaren Branches, Tags, Releases und Artefakte geprüft. Ein Embargoende löst die Gegenstandsprüfung aus. Freigegeben wird nur, was die dokumentierten Bedingungen erfüllt. Ein Dateiexport allein ist keine Rechteprüfung.

## 10. Sicherung und Bewahrung

H10 · Regel

IT sichert zentrale Repos und benötigte Plattformdaten täglich; wöchentlich entsteht eine institutionell getrennte Sicherung. Monatlich wird die Wiederherstellung einer wechselnden Stichprobe protokolliert, jährlich ein vollständiger Bandaufbau. Datenbank-Snapshots, zusätzliche Binärdateien und benötigte Softwarebestandteile gehören dazu.

Das Bandmanifest verbindet Text, Register, Schema, Transformationen, Handbuch- und Profilversionen sowie Freigaben. Das wissenschaftliche Archiv übernimmt zitierfähige Publikationspakete und geschützte Prozesspakete getrennt. Prozesspakete enthalten auch erforderliche Entscheidungs- und Verfahrensdokumentation; ihre Zugänge werden gesondert geregelt.

## 11. Vorfälle, Ausscheiden und Rollenwechsel

H11 · Regel

Fehler werden mit Repo und Standkennung gemeldet, sensible Angaben im vertraulichen Meldekanal. Meldungen dienen zuerst der Schadensbegrenzung. Fachliche Fehler werden nachvollziehbar korrigiert; notwendige Sicherheits- oder Datenschutzbereinigungen koordiniert die zuständige Stelle einschließlich kontrollierter Kopien.

Beim Ausscheiden werden Aufgaben und offene Entscheidungen übergeben, Zugänge gesperrt und lokale Kopien nach IT-Anweisung gelöscht oder institutionell übernommen. Beiträge bleiben nach den vereinbarten Anerkennungsregeln sichtbar. Datenschutzanträge werden gesondert geprüft; das Ausscheiden macht die Arbeitsgeschichte weder automatisch öffentlich noch automatisch gegenstandslos.

Lokale Git-Stände und das .git-Verzeichnis bleiben vor unbefugtem Zugriff geschützt. Geräteverlust, verlorene Datenträger, versehentliche Freigaben oder möglicherweise kopierte Daten werden unverzüglich gemeldet; ein nachgewiesener Datenabfluss wird nicht abgewartet.

Bei Rollen- und Institutionswechsel werden Aufgabe, Vereinbarung und benötigte Zugriffe vor der Weiterarbeit neu geprüft. Befristete Ausnahmen für verbleibende Zugänge oder Kopien brauchen dokumentierten Zweck, Umfang, Schutz, Ablaufdatum und Freigabe der Gesamtkoordination unter Beteiligung der zuständigen Stellen. IT dokumentiert die Umstellung und spätere Abschlusskontrolle.

## 12. Empfehlungen und Kontaktwege

H12 · Empfehlung und Verzeichnis

Empfehlung: häufig kleine verständliche Zwischenstände sichern und lange unsynchronisierte Arbeit vermeiden. Die Commitfrequenz ist kein Leistungsmaß. Bei Unsicherheit früh eine Fachperson einbeziehen.

Git, Profile und Übergaben: wissenschaftlich-technische Redaktion. Fachliche Entscheidungen: zuständige Bandredaktion. Rechte und Verlag: Rechte-/Publikationsstelle. Sicherheitsvorfälle: institutioneller IT-Service. Personenbezogene Daten und Einwände: Datenschutzstelle und Mitarbeitendenvertretung. Die aktuelle Kontaktliste liegt geschützt im Projektportal.

Verbindliche Anlagen: Zuständigkeitsmatrix, Editionsrichtlinie, ODD/Schema, Prüfregeln, oXygen-Profilbeschreibung, Reviewvorlage, Rechteverzeichnis, Sicherungs-/Archivprofil und Mitarbeitervereinbarung. Der freigegebene Stand jeder Anlage ist verzeichnet.

## Änderungsnachweis

- **1.0** Erste gemeinsame Arbeitsordnung: Prüfung vor Übergaben, Review, Publikation und Sicherung.
- **1.1** Nach BUG-58: sofortige Rückimportkontrolle H06 als Übergangsregel freigegeben; parallel Toolüberarbeitung und Regressionstest beauftragt. Nach Abnahme des Tools wird die Regel erneut geprüft.
