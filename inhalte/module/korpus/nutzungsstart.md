# Rätselhaft! – vom Download zur ersten Untersuchung

Künstlicher Übungsbestand · Demo-0.2 · keine historischen Belege.

Dieses kleine Paket funktioniert lokal mit Python 3.10 oder neuer, ohne Zusatzpakete, API, Konto oder Netzverbindung. Dateien gemeinsam in einen Ordner entpacken. Im Terminal in diesem Ordner ausführen:

```
python untersuchen.py
```

Erwartet: drei Rätsel, drei zugeordnete Lösungen; ein Reimpaarrätsel, eine versifizierte Lösung und ein ausgespartes Reimwort. Das Programm schreibt `ergebnis.json`, `testeingaben.jsonl` und `loesungen.jsonl` nach `ausgabe/`.

## Was gehört wohin?

- `korpus.xml`: maßgeblicher TEI-Beispielbestand mit stabilen Kennungen. Lösungen sind getrennt abgelegt und über corresp verbunden.
- `untersuchen.py`: Auswahl, Bestands-/Verweisprüfung und zwei getrennte Exporte. Es prüft kein TEI-Schema. Die Prüfungen für den anderen Beispielbestand liegen im übergeordneten Paket.
- `ausgabe/testeingaben.jsonl`: Rätseltexte und IDs ohne Lösungen. Diese Datei kann ein Modellversuch als Eingabe verwenden.
- `ausgabe/loesungen.jsonl`: getrennte Referenzlösungen für die anschließende Auswertung; nicht dem Modell in die Testeingabe geben.
- `ausgabe/ergebnis.json`: Auswahl, Demo-Datenfassung, erwartete Bestände und ausgeführte Prüfungen.

Die Texte, Kennungen und Kategorien sind für diese Übung erfunden. Die Kategorien sind nicht gegenseitig ausschließend. Dieses Miniaturkorpus ist kein wissenschaftlicher Benchmark. Es illustriert die Paket- und Versuchstrennung; es führt kein Sprachmodell aus und bewertet keine Modellleistung.

## Eine Seminaraufgabe

Vergleichen Sie das dritte Rätsel mit einer selbst erstellten Prosafassung ohne Reimhinweis. Halten Sie diese als Bearbeitung getrennt vom Original fest. Formulieren Sie vor dem Modellversuch eine Hypothese und eine Auswertungsregel. Welche Bedeutung haben unterschiedliche Schreibungen und mehrere plausible Antworten?

Für einen tatsächlichen Benchmark: Datenrelease und Auswahl nennen, Modell-/Werkzeugfassung und Parameter festhalten, Trainings- und Testbestand einschließlich verwandter Belege prüfen und Auswertungsregeln dokumentieren. Der vollständige Korpusdownload sollte denselben Strukturregeln folgen wie der kleine Einstieg.

## Nutzungsrechte

Die für diese Demonstration neu verfassten drei Rätseltexte und das Beispielskript dürfen unter CC0 1.0 verwendet werden: https://creativecommons.org/publicdomain/zero/1.0/ . Historische Daten eines wirklichen Projekts brauchen eine eigene Rechte- und Lizenzklärung.
