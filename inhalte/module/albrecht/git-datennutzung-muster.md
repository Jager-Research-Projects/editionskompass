# Anlage: Prozessanalysen mit Git

Stand: 0.4.1 – 2026-10-21

Diese Anlage konkretisiert Abschnitt 5 der Mitarbeitervereinbarung. Sie regelt Untersuchungen zur Verbesserung der Arbeitsabläufe. Eine neue regelmäßige Analyse beginnt erst nach dokumentierter Frage, Information und erforderlicher Freigabe.

- Verantwortlich: Gesamtkoordination Eva Brandt
- Technische Durchführung: Samir Demir und benannte Vertretung
- Fachliche Prüfung: zuständige Bandredaktion
- Einwände und Datenschutz: Datenschutzstelle des Akademienverbunds / Mitarbeitendenvertretung
- Überprüfung: halbjährlich sowie vor jeder Zweck- oder Methodenerweiterung

## 1. Frage und Umfang

Eine Analyse beschreibt Arbeitsschritte und Fehlerklassen. Rohdaten werden nur im erforderlichen Umfang gelesen. Berichte enthalten keine personenbezogenen Ranglisten. Die Rekonstruktion einzelner Änderungen wird nicht als vollständiger Nachweis von Ursache oder Verantwortung ausgegeben.

## 2. Zugriff, Weitergabe und Fristen

Samir und seine Vertretung bearbeiten die freigegebenen Untersuchungsdaten in der geschützten Arbeitsumgebung. Nora prüft die fachliche Einordnung. Eva und die betroffenen Fachredaktionen erhalten den auf Prozessbefunde begrenzten Bericht. Verlag und Gutachtende erhalten keine personenbezogenen Rohdaten.

Analyseexporte werden 90 Tage nach Abschluss gelöscht. Der fachlich geprüfte Prozessbericht wird zwei Jahre vorgehalten und dann auf weiteren Bedarf geprüft. Wissenschaftliche Quellhistorien unterliegen dem gesonderten Archivkonzept. Gesetzlich erforderliche abweichende Aufbewahrung wird getrennt dokumentiert.

## 3. Ausgeschlossene Nutzungen

Individuelle Arbeitszeiten, Leistungsrankings und automatische Personalentscheidungen werden nicht abgeleitet. Zeitstempel dürfen in der hier freigegebenen Fehlersuche die Reihenfolge rekonstruieren; eine neue Auswertung von Tageszeiten oder individuellen Arbeitsmustern ist dadurch nicht erlaubt. Pseudonyme Daten werden nicht als anonym behandelt.

## 4. Änderung, Einwände und Altdaten

Neue Methoden, Empfänger oder Zwecke werden vorab mit dem Team besprochen und institutionell geprüft. Ältere Daten werden nur nach gesonderter Prüfung von Zweck, Notwendigkeit und Informationspflichten einbezogen. Diese Anlage erteilt keine rückwirkende Zustimmung. Strittige neue Auswertungen werden bis zur Klärung ausgesetzt.

## Analyseblatt BUG-58: Der fehlerhafte Rückimport

- Frage: Verändert die Kommentaroberfläche geprüfte Zeichen und Zeitraumauszeichnungen?
- Daten: die betroffenen Kommentare und passende Gegenbeispiele des aktuellen Bandes; Fassungen vor und nach Rückimport, Schema-/Registerregel und Prüfabzug.
- Methode: git blame/show und Fassungsvergleiche; Vergleich nach Bearbeitungsweg und Fehlerklasse. Tageszeiten und individuelle Arbeitsmuster werden nicht ausgewertet.
- Durchführung: Samir und technische Vertretung; fachliche Abnahme: Nora. Eva und die betroffenen Redaktionen erhalten den Prozessbericht.
- Umgebung: institutionelles GitLab und lokale XML-Auswertung; kein Upload an externe Analyse- oder KI-Dienste. Exportlöschung 90 Tage nach Abschluss, Berichtprüfung nach zwei Jahren.
- Maßnahmen: Übergangsprüfung H06 sofort anwenden, das Kommentartool parallel überarbeiten und den Rückweg mit Regressionstest abnehmen; anschließend das Handbuch erneut prüfen. Die frühere Nachtbeobachtung wird nicht zur Routine und ist kein Bestandteil dieses Analyseauftrags.

## Einordnung und Quellen

[EDSA: Grundsätze für die Verarbeitung](https://www.edpb.europa.eu/topics/key-gdpr-concepts/basic-principles_de) · [EDSA: Rechtsgrundlagen und Einwilligung](https://www.edpb.europa.eu/sme/be-compliant/process-personal-data-lawfully_en) · [Österreichisches Beispiel: § 96 ArbVG](https://www.ris.bka.gv.at/Dokumente/Bundesnormen/NOR40123095/NOR40123095.html)

Die Anlage konkretisiert die Mitarbeitervereinbarung der Albrecht-Edition.
