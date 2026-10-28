# Früh zeigen. Bewusst freigeben.

Nicht alles muss bis zum Schluss warten. Das Team kann Kapitel, Bearbeitungsstufen oder einzelne Funktionen früher veröffentlichen – wenn es Umfang, Interessen und Freigaben gemeinsam plant.

## Ein Gespräch im Team

„Warum warten wir mit dem Frontend, bis der ganze Roman fertig ediert ist?“, fragt die Entwicklerin. „Register und Digitalisate könnten wir schon zeigen. Und einen freigegebenen Abschnitt gemeinsam ausprobieren.“ Falk sieht den Vorteil: Rückmeldungen kämen zu einer Zeit, in der das Team noch darauf reagieren kann.

Lukas zögert: „Meine neue Blattordnung ist noch nicht publiziert.“ Nora nickt. Auch der Verlag will den späteren Band nicht vollständig vorweggenommen sehen. Sie trennen deshalb die Fragen: Welche Funktionen dürfen schon online gehen? Welche Texte und Deutungen geben sie wann frei?

**Merken:** Frühe Teilveröffentlichungen brauchen einen eigenen Freigabeplan – nicht den vollständigen Abschluss der Edition.

## Früh entwickeln – eng an der Edition

Wir beginnen früh und iterativ, dosieren den Ausbau aber nach dem vorhandenen Material. Ein technisches Grundgerüst kann vom Projektstart an vorbereitet werden. Fachliche Ansichten wachsen mit einem repräsentativen TEI-Pilotbestand. So bleibt das Frontend nahe am jeweiligen Editionsstand, statt erst am Schluss auf einen vermeintlich endgültigen Bestand zu treffen.

Im Antrag folgt der Frontendausbau in unserem Fall mit leichter Überlappung auf die eigentliche Editionsarbeit. Das lässt wenig Zeit für fachliche Rückmeldungen vor Förderende. Falk stimmt deshalb zu Projektbeginn einen vorgezogenen technischen Vorlauf und feste Entwicklungsfenster mit der lehrstuhleigenen IT ab. Die vorhandene Kapazität wird neu eingeplant; zusätzliche finanzielle Lasten werden vermieden. Aufgaben und Zeitbedarf werden im aktualisierten Arbeitsplan festgehalten.

**Leitlinie:** Beginnen: so früh wie möglich, so spät wie nötig. Kernfunktionen rechtzeitig abnehmen; danach so lange optimieren, wie vereinbarte Kapazität verfügbar ist.

### 1 · Technischer Vorlauf ab Projektstart

Die Technik bereitet Grundgerüst, Datenzugriff, gegebenenfalls die vorgesehene Datenbankanbindung und den IIIF-Zugang vor. Testdaten prüfen Schnittstellen und Abläufe. Wissenschaftliche Mitarbeit ist auf die nötigen Grundentscheidungen begrenzt; ausgedachte Testdaten bestimmen keine Editionshypothesen.

### 2 · Fachlicher Ausbau mit repräsentativer TEI

Der Pilot enthält typische und schwierige Fälle: Randzusatz, Streichung, unklare Zuordnung und stabile Bildanker. Dieser begrenzte Modellbereich ist ausreichend beschrieben, bevor die zugehörigen Ansichten ausgebaut werden. Das gesamte TEI-Modell muss noch nicht endgültig sein. Veränderte Regeln bekommen einen versionierten Schnittstellenstand und passende Tests.

### 3 · Kurze Ausbau- und Rückmeldefenster

Fachredaktion und Technik prüfen überschaubare Ansichten am aktuellen Editionsstand. Rückmeldungen werden gebündelt; nicht jede Alltagskorrektur wird zur Frontendbesprechung. Die Technik arbeitet in vereinbarten Fenstern statt über die gesamte Laufzeit durchgehend gebunden zu sein. Öffentliche Freigaben folgen zusätzlich den Absprachen mit Verlag und Forschenden.

### 4 · Kernabnahme vor Förderende, Optimierung danach im vereinbarten Rahmen

Die nötigen Kernfunktionen werden mit Zeit für Korrekturen abgenommen. Weitere Optimierungen laufen solange Personal und technische Kapazität verfügbar sind. Bei einem früher nötigen Entwicklungsende gibt es einen lauffähigen, beschriebenen Stand. Fortgesetzte Entwicklung nach Stellenende erhält eine eigene Zuständigkeit und Kapazitätszusage.

### Aufwand bewusst begrenzen

**TEI bleibt in Bewegung:** Ein sofortiger Vollausbau kann unnötige Umbauten erzeugen. Deshalb beginnen wissenschaftliche Ansichten mit einem tragfähigen Modellbereich und einem realen Pilotbestand; Schema, Daten und Code werden gemeinsam getestet.

**Facharbeit braucht Ruhe:** Ständige Oberflächendiskussionen ziehen Energie von Transkription und Modellierung ab. Das Team bündelt Anforderungen, benennt eine Ansprechperson und begrenzt Rückmeldungen auf vereinbarte Termine.

**Entwicklung bindet Zeit:** Auch vorhandene IT-Kapazität ist einzuplanen. Technischer Vorlauf, Ausbau und spätere Korrekturen erhalten feste Fenster. Ziel ist lange Verbesserbarkeit, keine dauernde Vollzeitbindung des Entwicklungsteams.

### So stützt Git beide Entwicklungswege

Wir richten dieselbe Prüfgrundlage ein. Im iterativen Weg wird sie häufig durchlaufen; im Phasenmodell sichert sie die Übergaben und die anschließende Integration. Technisches Prüfen und fachliches Gegenlesen gehören zusammen.

### Iterativ: kleine Änderungen, häufig zusammen prüfen

1. Für eine überschaubare Aufgabe einen kurzen Branch anlegen, etwa für die Anzeige von Randzusätzen. Im Änderungsvorschlag (Merge Request) stehen erwartetes Verhalten und die betroffenen Beispielstellen.
2. Bei jedem Änderungsvorschlag lässt die GitLab-Pipeline automatisch prüfen: Passen TEI und Schema zusammen? Bleiben Kennungen und Bildverweise erhalten? Lässt sich das Frontend bauen? Zeigt der Interface-Test den Randzusatz an der richtigen Stelle? Die Technik erzeugt daraus eine zugangsgeschützte Testansicht für die Redaktion.
3. Nach erfolgreicher Prüfung und fachlicher Rückmeldung wird die Änderung in den Hauptstand übernommen. Bei einer Modelländerung prüfen wir auch die zugehörige Anpassung des Frontends. Das Integrationsprotokoll hält fest, welche Daten-, Schema- und Code-Commits gemeinsam getestet wurden.

**Beispiel:** Nora meldet: Der Randzusatz fehlt im Interface. Der Änderungsvorschlag ergänzt Ansicht und Testfall. Danach prüft Nora genau diese Stelle in der Testansicht; die Pipeline prüft zusätzlich die bisherigen Beispielfälle.

### In Phasen: Übergaben eindeutig und wiederholbar machen

1. Schon während der Editionsphase vereinbaren Redaktion und Technik das Übergabeformat. Schema, repräsentative TEI-Beispiele und erwartete Ausgaben liegen versioniert vor. Automatische Prüfungen melden Abweichungen, auch wenn der eigentliche Frontendausbau erst später beginnt.
2. Am Phasenende kennzeichnen wir den abgenommenen Lieferstand mit einem annotierten Tag, etwa tei-uebergabe-01. Das Übergabeprotokoll nennt zusätzlich den genauen Commit, das Schema und bekannte offene Punkte. Die Entwicklung bezieht ausdrücklich diesen Stand, nicht laufend den neuesten Arbeitsstand.
3. Der erste Integrationslauf baut das Frontend gegen diese Grundlage und prüft die vereinbarten Beispielfälle. Korrekturen laufen als kurze Änderungsvorschläge in die maßgeblichen Daten zurück. Ein neuer Übergabestand ersetzt den alten erst nach erneuter gemeinsamer Prüfung; wir verschieben den alten Tag nicht.

**Beispiel:** Die Redaktion liefert TEI-Stand 01. Während die Technik damit arbeitet, wird eine Bildreferenz korrigiert. Die Korrektur bekommt einen eigenen Änderungsvorschlag und anschließend einen neuen Übergabestand. So ist erkennbar, welche Fassung die Entwicklung tatsächlich verwendet.

### Hooks: früh am Arbeitsplatz prüfen

Ein pre-commit-Hook prüft vor dem Speichern eines Commits die dafür vorgemerkten XML-Dateien und meldet etwa ungültige Auszeichnung oder doppelte Kennungen. Die Technik hält Hook und Prüfscripte im Repo, richtet sie beim Onboarding ein und dokumentiert die benötigten Werkzeuge. Lokale Hooks müssen auf jedem Arbeitsplatz aktiviert werden und können umgangen werden. Deshalb wiederholt die zentrale Pipeline die verbindlichen Prüfungen.

### Pipeline: den gemeinsamen Stand absichern

Die Pipeline ist ein auf dem GitLab-Server eingerichteter Prüfablauf, kein eingebauter XML-Prüfer von Git. Wir versionieren ihre Konfiguration und verwenden festgelegte Werkzeugversionen. Automatische Tests prüfen auch die Kombination der vorgesehenen Daten-, Schema- und Codefassungen aus den getrennten Repos. Der Hauptbranch ist geschützt; Übernahmen erfordern erfolgreiche Pflichtprüfungen und die vereinbarte Durchsicht. Testberichte und Testansicht bleiben im berechtigten Team. Ein grüner Test ersetzt keine editorische Abnahme.

### Markieren, wiederholen, gezielt zurücknehmen

Für jeden abgenommenen Integrationsstand verzeichnen wir die exakten Daten-, Schema- und Code-Commits sowie Bauanleitung und Werkzeugversionen. Tags machen solche Meilensteine gut auffindbar. Prüfergebnisse und Testansichten werden passend dazu gesichert; kurzlebige Pipeline-Artefakte sind kein dauerhaftes Archiv. Verursacht eine Änderung einen Fehler, kann git revert sie durch einen neuen, nachvollziehbaren Commit zurücknehmen. Anschließend wird die Kombination erneut geprüft. Getrennte Repos werden dabei ausdrücklich aufeinander abgestimmt.

**Der erste konkrete Auftrag:** Die Technik richtet zunächst einen versionierten Prüfaufruf für lokale Hooks und Pipeline ein. Die Redaktion liefert dazu typische und schwierige Beispielstellen samt erwarteter Darstellung. Gemeinsam erproben sie einen gültigen und einen absichtlich fehlerhaften Teststand sowie den erneuten Aufbau eines bezeichneten Integrationsstands.

**Erledigt, wenn:** Ein Änderungsvorschlag mit fehlerhaftem Testmaterial wird zuverlässig gestoppt; ein zulässiger Stand lässt sich anhand seiner Daten- und Codekennungen erneut bauen und fachlich prüfen.

Technische Grundlagen: [Git: Hooks](https://git-scm.com/docs/githooks) · [GitLab: CI/CD-Pipelines](https://docs.gitlab.com/ci/pipelines/)

## Drei Wege, die sich kombinieren lassen

### Funktionen zuerst

Register, Digitalisatsansicht oder Volltextsuche werden nutzbar, bevor die edierten Texte vollständig vorliegen.

**Beispiel:** Ein freigegebenes Register erschließt Manuskriptseiten. Die Suche arbeitet zunächst auf einem bezeichneten Transkriptionsbestand und führt zum Digitalisat.

**Git-Strategie:** Frontendcode, Suchindex, Register und Datenbasis erhalten getrennte Versionsbezüge. Die öffentliche Kombination wird als getesteter Integrationsstand freigegeben.

**Vor der Freigabe:** Auch Register, Suchindex, Treffertexte und Bildzugänge gehören in die Freigabe. Noch nicht veröffentlichte Interpretation wird daraus nicht ungeprüft sichtbar.

### Kapitelweise veröffentlichen

Ein geprüfter Teilbestand wird als benannte Teilausgabe veröffentlicht; weitere Kapitel kommen später hinzu.

**Beispiel:** Ein erstes Kapitel mit seinen Entwurfsfassungen erscheint, während andere Konvolute noch bearbeitet werden.

**Git-Strategie:** Jeder Release verzeichnet die enthaltenen Einheiten und ihre Modell-/Prüfstände. Die Ausgabe bleibt zitierbar, auch wenn weitere Kapitel folgen.

**Vor der Freigabe:** Mit Verlag und Forschenden werden Textumfang, Varianten, Kommentare und Zeitpunkt vereinbart. Fehlende Kapitel werden im Inhaltsverzeichnis erkennbar gemacht.

### Bearbeitungsstufen zeigen

Zuerst wird eine geprüfte Basistranskription publiziert; genetische Auszeichnung und Kommentare folgen in neuen Fassungen.

**Beispiel:** Version 0.1 bietet eine geprüfte Transkription. Version 0.2 ergänzt eine erste ausgewiesene Annotationsschicht; später folgt die vollständig verantwortete genetische Darstellung.

**Git-Strategie:** Transkription, Annotation und fachliche Freigabe werden pro Einheit dokumentiert. Neue Fassungen ersetzen die zitierte ältere Ausgabe nicht stillschweigend.

**Vor der Freigabe:** Eine Transkription wird als Transkription bezeichnet, nicht als fertige genetische Edition. Zusätzliche Annotationen erhalten einen eigenen Stand und Prüfstatus.

## Verlag und Dissertationen

Der Verlag möchte das gedruckte Buch nicht lange vor seinem Erscheinen vollständig vorweggenommen sehen. Lukas und Nora möchten Zeitpunkt und Form ihrer eigenen Forschungspublikationen mitbestimmen. Deshalb legt das Team für jede Teilausgabe fest, welche Texte, Register, Suchtreffer, Kommentare und Deutungen öffentlich werden. Internes Ausprobieren kann früher beginnen: Tests und Rückmeldungen sind auch mit einem begrenzten Zugang möglich. Die vereinbarten öffentlichen Teile gehen anschließend gezielt online.

## Alternativszenario: kumulative Dissertationen

In einem alternativen Szenario vereinbaren Lukas und Nora eine kumulative Promotion: Zusammengehörige wissenschaftliche Beiträge entstehen und erscheinen während der Forschungsarbeit. Eine frühe, klar verantwortete Veröffentlichung kann dann im eigenen Interesse liegen. Lukas könnte seine neue Rekonstruktion in einem eigenständigen Beitrag begründen; Nora ihre Figurenanalyse mit einer veröffentlichten Annotationsfassung verbinden. Beide können auf die passende Ausgabe der Webedition verweisen. Welche Publikationsformen, Begutachtung und Eigenanteile zählen, wird früh mit Betreuung und zuständiger Fakultät nach der geltenden Promotionsordnung geklärt. Das kann den Druck mindern, alles bis zu einer einzigen abschließenden Publikation zurückhalten zu müssen.

## Zitieren und Beiträge zuordnen

Für eine konkrete Analyse wird eine archivierte Ausgabe mit Versions-DOI zitiert; Stellenkennungen verweisen auf die untersuchte Passage. Auf der Website stehen Autorenschaft und Verantwortungsanteile beim jeweiligen Beitrag. Die weiterentwickelte Edition verlinkt die ältere Fassung und den Beitrag. Ein DOI macht den Stand referenzierbar; die Anerkennung als Promotionsleistung richtet sich nach den vereinbarten fachlichen und formalen Anforderungen.

## So würden wir beginnen

Wir entwickeln das Frontend früh und iterativ. Grundgerüst und Schnittstellentests können zu Projektbeginn entstehen; der fachliche Ausbau beginnt mit repräsentativen TEI-Daten. In vereinbarten Rückmeldefenstern halten wir die digitalen Ansichten eng am jeweiligen Editionsstand. Kernfunktionen nehmen wir rechtzeitig vor Förderende ab und optimieren weiter, solange Kapazität verfügbar ist. Ein freigegebener öffentlicher Funktionsumfang kann früh nutzbar werden; Kapitel und Bearbeitungsstufen folgen nach den vereinbarten Freigaben. Für Betrieb und Pflege ist ein Kontakt benannt. Der Satz liegt beim Verlag; eigene frühe Satzpreviews gehören in diesem Modell nicht zum Projektablauf.

1. Technischen Vorlauf und Entwicklungsfenster im Arbeitsplan vereinbaren; einen repräsentativen TEI-Pilotbestand und einen begrenzten Modellbereich festlegen.
2. Ansichten am aktuellen Editionsstand erproben; Rückmeldungen bündeln und öffentliche Freigaben mit Verlag und Promovierenden abstimmen.
3. Kernfunktionen mit Testpuffer abnehmen; weitere Teilreleases, Archivbezüge, Optimierungen und verfügbare Anschlusskapazität dokumentieren.

**Erledigt, wenn:** Ein erstes vereinbartes Angebot ist öffentlich nutzbar, sein Umfang und Datenstand sind erkennbar, Rückmeldungen haben einen zuständigen Empfänger und die nächste Ausgabe hat eine konkrete Aufgabe.

## Hintergrund und Quellen

- [Kumulative Dissertation · Philosophische Fakultät Göttingen](https://www.uni-goettingen.de/de/689605.html): Ein Beispiel auch für Neuere deutsche Literatur und Digital Humanities. Die Anforderungen unterscheiden Publikationsfähigkeit und individuelle Beiträge; maßgeblich ist die jeweilige Promotionsordnung.

- [Zenodo · DOI-Versionierung](https://zenodo.org/help/versioning): Versions-DOIs referenzieren eine bestimmte Ausgabe; ein übergreifender DOI kann alle Versionen repräsentieren.
