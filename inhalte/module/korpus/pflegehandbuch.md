# Lokaler Übergabetest – ausführbare Arbeitsanleitung

## 1. Auftrag und Grenzen

Ein unbekannter Arbeitsrechner soll die Demonstration ohne persönliche Konfiguration der bisherigen Bearbeiterin ausführen können. Dies ist ein lokaler Probe-Release. Keine Konten verwenden, keine DOI anlegen, keine Daten hochladen. Für produktive Archivierung gelten benannte Freigaben und institutionell übergebene Zugänge.

## 2. Umgebung

Das komplette Beispielpaket in einen frischen Ordner entpacken. Python 3 und die in requirements.txt bezeichnete lxml-Fassung verwenden. Installationsweg und Versionen dokumentieren; Zugangsdaten gehören nicht in dieses Handbuch.

## 3. Ausführen

Im Verzeichnis mit dieser README und run_demo.py:

```text
python run_demo.py
```

Der Lauf nutzt ausschließlich die beiliegenden Dateien. Er prüft Schema, Kennungen und vorhandene Verweise, den Quellenregressionstest, die zwei Bestände sowie die beiden Extraktionen und erzeugt einen Probe-Release.

## 4. Erwartete Ergebnisse

- Fehlerhafter Import: vier vermeintliche Rätsel, keine zugeordneten Lösungen; formale Checks bestanden, Quellenregression nicht bestanden.
- Korrigierter Import: zwei Rätsel, zwei korrekt referenzierte Lösungen; beide Prüfebenen bestanden.
- Demo-v1.0: zwei Versrätsel unter vier Rätseln = 50 Prozent.
- Demo-v1.1: acht Versrätsel unter zehn Rätseln = 80 Prozent.
- Die vier ursprünglichen Belege ergeben auch im neuen Stand weiterhin 50 Prozent.
- Nur-Rätsel-Extraktion enthält nicht „Der Kamm.“ als Lösung. Die breitere Extraktion enthält die Antwort.
- probe-release.zip kann geöffnet werden; sämtliche Dateien stimmen mit den manifestierten SHA-256-Werten überein.

## 5. Fehlerhilfe

Fehlendes lxml: richtige Python-Umgebung und requirements.txt prüfen. Schemafehler: konkrete Datei und Fehlermeldung lesen, keine Prüfung abschalten. Unerwartete Zahlen: Datenordner und Auswahl mit dem Manifest abgleichen. Fehlende Datei im Paket: Paket neu erzeugen und Vollständigkeit prüfen; eine Liste ersetzt keine tatsächlichen Dateien.

## 6. Menschlicher Übergabetest

Eine andere Person führt die Schritte ohne Zuruf aus und notiert unklare Stellen. Bestätigt werden nur tatsächlich ausgeführte Schritte, Umgebung und Ergebnis. Der beigefügte automatische Neuaufbau ist bereits geprüft; ein unabhängiger menschlicher Übergabetest ist noch durchzuführen.

## 7. Verantwortung nach Förderung

Im fiktiven Projekt verantwortet Miriam wissenschaftliches Profil und Pflegezusagen; Jonas und eine benannte Vertretung führen die technischen Aufgaben aus, Tessa berät bei Archivierung und Metadaten. Institutionelle Owner-/Kontaktrollen werden vor Leas Ausscheiden bestätigt. Ein technischer Zugang ist kein unbefristetes persönliches Pflegeversprechen. Neue Beiträge werden entsprechend der konservierenden Pflegezusage beurteilt.
