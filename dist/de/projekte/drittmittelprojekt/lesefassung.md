# Die andere Stadt

## Ein Roman in vielen Fassungen. Ein Projekt mit vier Zeitplänen.

Redaktioneller Prüfstand 0.4.2 · 2026-10-23

Die andere Stadt, Elise Hartmann und das Editionsteam sind fiktiv. Die Beispiele sind eigens angefertigtes Lehrmaterial.

---

## Das Projekt

Elise Hartmann (1842–1901) arbeitete zwischen 1878 und 1886 an ihrem Roman *Die andere Stadt*. Darin verändert die Industrialisierung eine Stadt – und mit ihr die Lebenswege und Beziehungen ihrer Bewohner. Hartmann begann mehrfach neu, verschob Kapitel und ließ Figuren verschwinden. Einzelne Kapitel erschienen vorab in Zeitschriften; der Roman blieb unvollendet und wurde nie als Buch veröffentlicht.

Im Nachlass liegen Notizhefte, zwei Manuskriptkonvolute und eine überarbeitete Reinschrift. Streichungen, Randzusätze und abweichende Blattfolgen erzählen unterschiedliche Geschichten seiner Entstehung. Welche Entwürfe gehören zusammen? Was wurde wann verändert? Miriam Falks Team will diese Zusammenhänge in einer genetischen Edition sichtbar und am digitalisierten Manuskript nachvollziehbar machen. Der gedruckte Band bietet eine begründet gewählte Lesefassung und ausgewählte Varianten.

Lukas untersucht die Werkgenese; Nora verfolgt, wie sich Figuren und Erzählperspektiven verändern. Beide arbeiten zugleich an eigenen Dissertationen. Vier Jahre sind finanziert. Doch die Forschung, der Verlagssatz und die digitale Veröffentlichung folgen ihren eigenen Zeitplänen.

**Leitfrage:** Wie bleibt eine gemeinsame Editionsgrundlage verlässlich, wenn Forschungen, Veröffentlichungen und Zuständigkeiten auseinanderlaufen?

---

## Was das digitale Frontend erschließt

In welcher Reihenfolge standen die Sätze zunächst? Wohin wurde eine Passage verschoben? Welche Ergänzung gehört zu welcher Schreibphase? Im Interface der digitalen Edition lassen sich Rekonstruktionen nebeneinander betrachten, einzelne Schichten einblenden und direkt mit der Handschriftenseite vergleichen. Der gedruckte Band vermittelt ausgewählte Varianten und eine begründete Lesefolge; wechselnde Anordnungen und konkurrierende Rekonstruktionen lassen sich dort schwerer nachvollziehen. Die wissenschaftlich verantworteten TEI-Daten halten Texte, Varianten und editorische Beziehungen unabhängig von einer einzelnen Oberfläche fest. Sie bilden den Kern unserer digitalen Edition und können unterschiedliche Frontends, Druckausgaben und weitere Forschungsanwendungen speisen. Das technische Frontend stellt dafür ein Interface zur Erschließung der digitalen Edition bereit: Seine Auswahl-, Vergleichs- und Bildfunktionen prägen, was sich an der Edition erkennen lässt.

---

## Gleiche Worte. Andere Lesefolge.

Eine Randnotiz kann unterschiedlich in den Haupttext eingeordnet werden. Wechseln Sie zwischen zwei Rekonstruktionen und wählen Sie einen Textteil: Seine Stelle auf der Demoseite bleibt auffindbar.

### Rekonstruktion A

Zuerst Clara am Tor, dann die dunkler werdende Stadt: Die Randnotiz wird nach Claras Ankunft eingeordnet.

1. Clara blieb am Tore stehen.
2. Hinter den Fenstern wurden die Lampen gelöscht.
3. Erst jetzt hörte sie die Schritte auf dem Pflaster.

### Rekonstruktion B

Zuerst die dunkler werdende Stadt, dann Clara am Tor: Dieselbe Randnotiz eröffnet die Passage. Der Zusammenhang wird anders gewichtet.

1. Hinter den Fenstern wurden die Lampen gelöscht.
2. Clara blieb am Tore stehen.
3. Erst jetzt hörte sie die Schritte auf dem Pflaster.

Die digitale Edition kann unterschiedliche Lesefolgen am selben Material erkundbar machen. Der Druck wählt eine begründete Folge und erläutert Alternativen im Apparat.

**Git-Bezug:** Git hält fest, welche Textteile, Zuordnungen und Modellregeln einer Ansicht zugrunde liegen. Die historische Reihenfolge ist eine editorische Hypothese; sie wird nicht aus der Abfolge moderner Commits abgelesen.

---

## So würden wir es machen

1. Das Team beginnt an einem kleinen Konvolut. oXygen mit Git-Client und ein kurzer gemeinsamer Ablauf ermöglichen selbstständige Korrekturen; die Technik unterstützt bei Konflikten.
2. Das Editionsrepo liegt in einer institutionellen GitLab-Projektgruppe. Zwei benannte Personen können Administration und Wiederherstellung veranlassen.
3. Eine geprüfte Basistranskription wird kontrolliert nach TEI übernommen. Danach ist diese Einheit im Editionsrepo die maßgebliche wissenschaftliche Arbeitsfassung.
4. Editionsdaten und Frontendcode liegen in getrennten Repos. Versionierte Konverter bleiben zunächst im Editionsrepo. Definierte Exporte liegen im Importarchiv.
5. Lukas entwickelt eine dauerhaft alternative Rekonstruktion auf einem bezeichneten Forschungsstand weiter. Nora pflegt zusätzliche Figurenrelationen in einem eigenen Annotationsrepo.
6. Veröffentlichungen verbinden freigegebene Daten, Schema, Frontend und Bildbezüge. Wissenschaftlich relevante Satzkorrekturen werden kontrolliert in die TEI zurückgeführt.
7. Vor Stellenende sind Forschungszugänge, lokale Datenkopien, Nachredaktion, institutionelle Verantwortung und Wiederherstellung geregelt.

---

## Vier Zeitpläne

- **Förderung:** Die Projektstellen und volle Infrastruktur sind für vier Jahre gesichert. Die Satzmittel bleiben auch bei späterer Fertigstellung verfügbar.
- **Dissertationen:** Lukas hat vor Projektbeginn begonnen; Nora entwickelt und meldet ihr Vorhaben nach der Einstellung an. Der Antrag plant den Abschluss zum Projektende; voraussichtlich laufen beide Forschungen darüber hinaus weiter.
- **Buch:** Abschluss im Antrag zum Projektende. Satzkosten sind gedeckt; spätere fachliche Nachredaktion ist gesondert zu sichern.
- **Editionsfrontend:** Zum Projektende soll das technische Frontend bereitstehen. Sein Interface ermöglicht es, die digitale Edition zu lesen, Schreibschichten zu vergleichen und Textstellen mit den Digitalisaten zu verbinden. Die TEI-Daten können auch unabhängig davon veröffentlicht und genutzt werden. Für einen späteren Frontendstart vereinbaren Projekt, Bibliothek und Verlag vorab einen Ersatzweg: Der Verlag stellt eine einfache Leseansicht und den freigegebenen TEI-Stand als Download bereit. Umfang, Fassungsangabe, Aktualisierung und Zuständigkeiten werden festgehalten; genetische Vergleiche und Bildverknüpfungen des geplanten Interfaces sind damit noch nicht vollständig verfügbar.

---

## Wir müssen edieren, nicht Software entwickeln

*Zusammenarbeit · P04-S01*

„Wir brauchen eure XML-Dateien in Git“, sagt das technische Team. Falk schaut von ihren Unterlagen auf: „Warum reicht unser gemeinsamer Ordner nicht?“ Lukas kennt Git vom Hörensagen und denkt an Konflikte. Nora fragt lieber gleich: „Was muss ich dafür jeden Tag zusätzlich tun?“

Sie probieren es an einer einzigen Stelle. Nora korrigiert „Thore“ zu „Tore“, vergleicht die Änderung und hält fest, warum sie nötig war. Lukas prüft am Bild. Als Nora die alte Lesung noch einmal sehen möchte, ist sie sofort wieder da. „Gut“, sagt sie. „Aber den Ablauf schreiben wir auf.“

**Merken:** Ein guter Git-Ablauf macht das Team selbstständig und lässt Hilfe erreichbar bleiben.

### So würden wir es machen

Git hält Änderungen und ihre Beziehungen fest. Ein Commit sichert zunächst im lokalen Repo. Erst das Übertragen auf den Projektserver macht ihn dort verfügbar. Die fachliche Prüfung der Lesung ist ein eigener Schritt.

**Beispiel:** beispiele/lesung-vorher.xml → beispiele/lieferstand-v1.xml: Thore wird zu Tore; die historische Streichung und der Randzusatz bleiben erhalten.

1. Pilotkonvolut und einfachen täglichen Ablauf festlegen.
2. Sichern, Übertragen, Vergleichen und fachliche Prüfung gemeinsam ausprobieren.
3. Handbuch, Einführung und technische Vertretung einrichten.

**Erledigt, wenn:** Eine neue Mitarbeiterin kann eine TEI-Korrektur sichern, auf den Projektserver übertragen und zur fachlichen Prüfung geben.

**Wie hilft Git:** Git zeigt die geänderte Stelle, die Begründung und den vorherigen Stand. Das institutionelle GitLab stellt den gemeinsamen Zugang bereit.

### So arbeiten wir miteinander

Das Team vereinbart vor dem ersten Zugang, welche Daten für Editionsarbeit und Dissertationen genutzt werden dürfen, wie Beiträge zugeordnet werden und wer freigibt. Interne Stände und Git-Geschichte dürfen nicht unbefugt weitergegeben werden. Lokale Kopien werden geschützt; möglicher unbefugter Zugriff oder Geräteverlust wird sofort an die Projektleitung und den technischen Kontakt gemeldet. Die praktische Schrittfolge steht im versionierten Handbuch. Zur Einführung gehört eine Übung im oXygen-Git-Client.

**Begriffe zum Aufklappen:**

**Git und GitLab:** Git hält Dateistände und ihre Beziehungen fest. GitLab ist die gewählte Plattform für gemeinsamen Zugang, Prüfung und Projektorganisation.

**Commit und Übertragen:** Ein Commit hält ausgewählte Änderungen lokal mit einer Nachricht fest. Übertragen macht diese Änderungen auf dem Projektserver verfügbar.

**oXygen:** Der XML-Editor unterstützt die TEI-Bearbeitung. Ein gesondertes Git-Client-Add-on integriert Vergleich und Versionsarbeit; Installation und Zugang gehören zur Einführung.

---

## Noch einmal exportiert

*Import und Datenhoheit · P04-S02*

Die erste Handschrifteneinheit ist in TEI übernommen. Lukas hat eine gestrichene Formulierung und den Zusatz am Rand ausgezeichnet. Dann kommt ein neuer Export: Eine Hilfskraft hat in Transkribus die Lesung „Thore“ verbessert. „Dann nehmen wir einfach die neue Datei?“

Nora öffnet den Vergleich. Der verbesserte Text ist da. Die genetische Auszeichnung aus ihrer Editionsarbeit fehlt. Sie übernehmen die Lesung gezielt. Der Export bleibt als Herkunftsbeleg erhalten; die bereits bearbeitete TEI wird weitergeführt.

**Merken:** Nach der abgenommenen Übernahme wird diese Editionsdatei in Git weiterbearbeitet.

### So würden wir es machen

Der Übergang erfolgt Einheit für Einheit: Basistranskription prüfen, Export fixieren, Transformation dokumentieren, Import abnehmen. Das ist noch keine Publikationsfreigabe. Spätere Korrekturen aus Transkribus werden als Änderungsvorschläge verglichen; sie ersetzen keine bereits angereicherte TEI-Datei.

**Beispiel:** beispiele/erneuter-export.txt enthält eine bessere Lesung, aber keine genetische Struktur; lieferstand-v1.xml bewahrt die Streichung und den Randzusatz.

1. Exportstand und Transformationsfassung dokumentieren und sichern.
2. Text, Randzusätze, Kennungen und Bildbezug am Import prüfen.
3. Abnahme und spätere Korrekturregel ins Handbuch aufnehmen.

**Erledigt, wenn:** Für eine Einheit sind Herkunft, Überführung, Abnahme und maßgeblicher Bearbeitungsort nachvollziehbar.

**Wie hilft Git:** Git macht sichtbar, welche Auszeichnung ein neuer Dateistand verlieren würde. Der kontrollierte Vergleich erlaubt eine gezielte Übernahme.

### Zwei Entscheidungen statt eines Stichtags

Ein Dokument wechselt nach bestandener Importprüfung. Die reguläre Transkribus-Produktionsphase endet erst, wenn die vorgesehenen Einheiten übergeben sind und die Inventur stimmt. Ziel ist eine frühe gemeinsame TEI-Basis. Schwierige Seiten dürfen länger bildnah bearbeitet werden. Für den Pilotvergleich testen wir PAGE XML mit eigener versionierter Transformation gegen den verfügbaren direkten TEI-Export.

**Begriffe zum Aufklappen:**

**Transkribus, OCR und HTR:** Die bildnahe Umgebung unterstützt Erkennung und Korrektur. OCR betrifft gedruckte, HTR handschriftliche Texte. Der Export wird vor der TEI-Weiterarbeit geprüft.

**XML und TEI:** XML stellt strukturierte Daten dar. TEI bietet ein fachliches Vokabular zur Beschreibung von Texten; das Projekt legt seine konkrete Verwendung fest.

**Transformation:** Ein versioniertes Verfahren überführt eine Eingabestruktur in das benötigte TEI. Das Ergebnis muss am Ausgangsmaterial geprüft werden.

---

## Die Ergänzung fehlt

*Digitale Edition · P04-S03*

Auf dem Bildschirm steht: „Clara blieb am Tore stehen.“ Lukas zeigt auf den Rand der Handschriftenansicht: „Und wo ist der Rest?“ In der TEI steht die Ergänzung längst: „als gehörte sie nicht hierher“. Die aktuelle Ansicht zeigt sie trotzdem nicht.

Nora und die Entwicklerin prüfen dieselbe Stelle. Der Viewer verarbeitet den Randzusatz noch nicht. Sie ergänzen Darstellung und Test. In der veröffentlichten Edition bleibt bis zur gemeinsamen Prüfung der bisherige freigegebene Stand.

**Merken:** Daten, Schema und Darstellung müssen zusammen geprüft werden.

### So würden wir es machen

Die genetische Edition erschließt Veränderungen und Beziehungen am Manuskript. Eine Lesefassung ist eine mögliche Ansicht. Auch Streichungen, Ergänzungen und ihre Bildbezüge müssen erkundbar bleiben. Wir prüfen deshalb nicht nur gültiges XML, sondern auch, ob die wissenschaftlich wichtigen Informationen tatsächlich ankommen.

**Beispiel:** beispiele/lieferstand-v1.xml enthält del und add. Ein Prüffall muss sicherstellen, dass beide in der genetischen Ansicht zugänglich sind.

1. Eine repräsentative Stelle und die erwarteten Ansichten dokumentieren.
2. Datenregeln, Bildanker und Darstellung gemeinsam testen.
3. Veröffentlichte Daten- und Codefassungen im Manifest festhalten.

**Erledigt, wenn:** Die Ergänzung ist in der vorgesehenen Ansicht erreichbar und die veröffentlichte Kombination aus Daten, Schema und Frontend ist bezeichnet.

**Wie hilft Git:** Git versioniert Daten und Code. Freigaben verbinden geprüfte Stände; unfertige Änderungen gelangen nicht automatisch ins öffentliche Angebot.

### Zwei Geschichten derselben Stelle

Hartmann strich eine Formulierung und ergänzte einen Satzteil am Rand. Das gehört zur historischen Textgenese. Nora korrigiert heute eine Lesung, Lukas präzisiert die Auszeichnung: Das gehört zur modernen Bearbeitungsgeschichte in Git. Das Datum eines Commits datiert keine historische Schreibhandlung.

**Begriffe zum Aufklappen:**

**ODD und Schema:** Die projektspezifische TEI-Anpassung beschreibt das Modell. Ein daraus abgeleitetes Schema prüft vereinbarte Strukturen; die Interpretation bleibt fachlich zu prüfen.

**IIIF:** Gemeinsame Schnittstellen machen Bilder und ihre Präsentationsstruktur nutzbar. Ein Canvas bezeichnet eine Seite oder Ansicht; Regionen erlauben Verweise auf Ausschnitte.

**Automatische Prüfungen:** Prüfungen laufen bei Änderungen wiederholt ab. Sie erkennen etwa fehlerhafte Strukturen und Verweise. Eine grüne Prüfung ersetzt keine Prüfung der Lesung.

**Digitale genetische Edition:** Die Edition erschließt Entwürfe, Schreibschichten und Beziehungen mit digitalen Mitteln. Ihre wissenschaftlichen Funktionen gehen über eine bloße Online-Lesefassung hinaus.

---

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


---

## Lukas ordnet ein Blatt neu ein

*Eigenständige Forschung · P04-S04*

Lukas legt zwei Blattkopien nebeneinander. „Ich glaube, unsere Reihenfolge stimmt hier nicht.“ Ein Befund an der Blattfolge spricht dafür, dass die Clara-Passage später entstand als bisher angenommen. Ausgerechnet seine eigene frühe Rekonstruktion steht damit zur Diskussion.

Nora hört aufmerksam zu. Ihre Dissertation verfolgt, wann Clara aus dem Roman verschwindet. „Dann verändert das auch meine Deutung.“ Sie prüfen den Befund gemeinsam. Lukas entwickelt die alternative Ordnung zunächst in einem eigenen Forschungsbestand weiter; Nora hält fest, auf welcher Editionsfassung ihre Figurenbeziehungen beruhen.

**Merken:** Eigenständige Forschung braucht einen bezeichneten Ausgangsstand und Raum für andere Deutungen.

### So würden wir es machen

Ein kurzer Branch eignet sich für eine begrenzte Änderung, die zur Prüfung zurückkommen soll. Eine längerfristig andere Rekonstruktion erhält ein eigenes Forschungsrepo. Nora ergänzt ihre Figurenbeziehungen separat als Stand-off-Annotation: Die Verweise beziehen sich auf stabile Stellen und einen konkreten Editionsstand. Über eine Änderung der offiziellen Edition entscheidet die Fachredaktion nach wissenschaftlicher Diskussion.

**Beispiel:** beispiele/forschungsbezug.json trennt Lukas’ alternative Blattordnung von Noras zusätzlicher Figurenrelation.

1. Ausgangsrelease, stabile Kennungen und Forschungsfrage benennen.
2. Arbeitsform wählen: kurzer Branch, eigenständiger Bestand oder zusätzliche Annotation.
3. Übernahmen und geänderte Bezüge fachlich prüfen und dokumentieren.

**Erledigt, wenn:** Beide Dissertationen können ihren Datenbezug reproduzieren; die offizielle Edition wird nicht unbemerkt ummodelliert.

**Wie hilft Git:** Git bewahrt alternative Bearbeitungsverläufe und ermöglicht gezielte Vergleiche und Übernahmen. Wissenschaftliche Gültigkeit wird fachlich beurteilt.

### Fork, Branch und Berechtigung

Ein Branch ist ein paralleler Verlauf innerhalb eines Repos. Ein Fork ist eine auf der Plattform verknüpfte Abzweigung in einem eigenen Projekt; Sichtbarkeit und Zugriff hängen von den Plattformregeln ab. Vor dem Fork werden diese geprüft. Für dauerhaft eigene vertrauliche Forschung kann ein gesondert eingerichtetes Repo geeigneter sein. Ein Branch schützt keine privaten Dissertationsteile vor anderen Personen mit entsprechendem Repozugriff.

**Begriffe zum Aufklappen:**

**Branch:** Ein paralleler Bearbeitungsverlauf im selben Repo, etwa für eine begrenzte Änderung mit späterer Prüfung.

**Fork:** Eine auf der Plattform verknüpfte Abzweigung eines Repos in einem eigenen Projekt. Regeln für Sichtbarkeit und Zugriff müssen zur beabsichtigten Nutzung passen.

**Stand-off-Annotation:** Zusätzliche Auszeichnung wird getrennt gespeichert und verweist auf genau bezeichnete Stellen einer Basisfassung.

---

## Im Buch ist es schon korrigiert

*Publikationsstände · P04-S05*

In der Fahne steht noch „als gehörte sie nicht hierher“. Beim erneuten Blick auf die Handschrift erkennt Nora: „dorthin“ ist die bessere Lesung. Der Satz wird korrigiert. „Ist das auch schon in unseren Daten?“, fragt Falk. Noch nicht.

Das Team führt die Korrektur in die TEI zurück und gibt V2 frei. Das Buch bleibt im Satz; die Bibliothek kann das geplante Editionsfrontend noch nicht bereitstellen. Als Ersatzweg haben Projekt und Verlag eine einfache Leseansicht mit TEI-Download vereinbart. Der Verlag bereitet dieses Angebot vor. Für den TEI-Download vereinbaren sie ausdrücklich V2.

**Merken:** Buch, TEI und Webangebot brauchen nachvollziehbare Fassungsbeziehungen.

### So würden wir es machen

Die Redaktion prüft fachliche Satzkorrekturen und übernimmt sie in die Editionsdaten. Typografische Anpassungen werden getrennt behandelt. Ein Tag markiert den freigegebenen Git-Stand; ein Release beschreibt und bündelt ihn. Die Archivfassung erhält eigene Metadaten. Die reduzierte Verlagsansicht schafft Zugang, bietet aber nicht alle genetischen Vergleichs- und Bildfunktionen des geplanten Editionsfrontends.

**Beispiel:** beispiele/lieferstand-v1.xml → referenzstand-v2.xml: hierher wird zu dorthin. Die Satzkorrektur ist im Korrekturprotokoll bezeichnet.

1. Korrekturrückgabe und zuständige Nachredaktion vor Förderende vereinbaren.
2. Wissenschaftlich relevante Satzkorrekturen gezielt übernehmen und prüfen.
3. Buchbezug, TEI-Download und Webkombination mit tatsächlichen Fassungen kennzeichnen.

**Erledigt, wenn:** V2 enthält die Korrektur; Download und Publikationsbeschreibung nennen den richtigen Stand. Verantwortung für spätere Änderungen ist vereinbart.

**Wie hilft Git:** Git dokumentiert die Rückführung. Benannte Stände und ein Manifest verbinden Lieferfassung, Korrektur und Ausgabe.

### Wenn der Download zunächst hinterherhinkt

Muss der Verlag zunächst V1 anbieten, wird sie als Satz-Eingangsstand mit benanntem Korrekturstatus veröffentlicht. Nachgereichte V2 erhält eine neue Bezeichnung und einen Änderungshinweis. Keine vorhandene Fassung wird stillschweigend als identisch mit dem fertigen Buch ausgegeben. Der öffentliche Viewer wird erst nach seinem eigenen Test auf V2 umgestellt. Die Satzmittel bleiben gesichert. Die auslaufenden Projektstellen finanzieren dagegen nicht automatisch die weitere wissenschaftliche Nachredaktion.

**Begriffe zum Aufklappen:**

**Tag:** Eine benannte Markierung eines Git-Stands. Eine Markierung allein führt keine Prüfung durch und sichert keine unabhängige Archivierung.

**Release:** Eine beschriebene Ausgabe, die das Team nach seinen Regeln freigibt. Daten, Prüfergebnis und Versionshinweise gehören zusammen.

**Archivfassung:** Ein beschriebenes erhaltenes Paket mit Zuständigkeit und gegebenenfalls persistentem Identifikator; unabhängig von der laufenden Bearbeitung.

---

## Die Stelle endet. Die Dissertation nicht.

*Weiterarbeit · P04-S06*

Nora packt ihren Schreibtisch zusammen. An der neuen Universität wartet eine andere Aufgabe; ihre Dissertation nimmt sie mit. „Und die Figurenannotation?“, fragt Lukas. „Die auch“, sagt sie. „Aber wir testen den Zugang lieber jetzt.“

Sie prüfen gemeinsam, welche Daten Nora weiterverwenden darf und welche Kopien sie besitzt. Die Bibliothek übernimmt ein beschriebenes Archivpaket. Für Nachkorrekturen an der Edition bleiben Falk und die benannte Redaktion zuständig. Der technische Kontakt zeigt seiner Vertretung, wie ein geprüfter Stand wiederhergestellt wird.

**Merken:** Weiterarbeit wird vor dem Stellenende vorbereitet und praktisch geprüft.

### So würden wir es machen

Die neue Rolle wird dokumentiert: eigener Forschungszugang, offizielle Schreibrechte, Freigabe und Administration sind unterschiedliche Befugnisse. Die Vereinbarung regelt erlaubte Kopien, Schutz, Rückgabe oder Löschung sowie begründete Ausnahmen und die spätere assoziierte Mitarbeit. Derselbe Rollencheck gilt für externe Technik, Verlag und Bibliothek; ihre Vereinbarungen richten sich nach Aufgabe und Zugang.

**Beispiel:** beispiele/zugangsmatrix.json unterscheidet Kernteam, assoziierte Forschung, technische Betreuung und empfangende Einrichtungen.

1. Forschungsbestand, Nutzungsrechte und funktionierenden Zugang vor Stellenende prüfen.
2. Fachliche Nachredaktion, Administration, Bildbetrieb und Archiv getrennt zuordnen.
3. Wiederherstellung und eine begrenzte Nachkorrektur durch eine zweite Person testen.

**Erledigt, wenn:** Nora kann ihren vereinbarten Forschungsstand nutzen. Eine zweite qualifizierte Person kann den dokumentierten Editionsstand wiederherstellen und prüfen.

**Wie hilft Git:** Ein Git-Klon oder Bundle kann die Datengeschichte übertragen. Plattformfunktionen, Berechtigungen und externe Bilddienste werden zusätzlich gesichert oder neu eingerichtet.

### Was ein Hostwechsel zusätzlich verlangt

Neben Dateien und Git-Geschichte werden offene Aufgaben, Prüfkonfiguration, geschützte Freigaben, Zugänge und Verweise kontrolliert. Geheimnisse und Zugangsschlüssel werden gesondert sicher verwaltet. Eine Archivzusage enthält keine automatische Zusage für Frontendbetrieb oder wissenschaftliche Nachredaktion.

**Begriffe zum Aufklappen:**

**Migration:** Ein geregelter Umzug von Daten und Abläufen. Git-Geschichte und zusätzliche Plattformfunktionen werden getrennt geprüft.

**Verantwortung und Administration:** Fachliche Freigabe, Serververwaltung, Rechte an Daten und Betrieb sind unterschiedliche Aufgaben. Sie werden Personen beziehungsweise Einrichtungen zugeordnet.

---

## Zugehörige Arbeitsmaterialien

- [Musterstrategie](musterstrategie.md)
- [Ordnung, Handbuch und Vereinbarungen](handbuch.md)
- [Demostelle](assets/demostelle.zip)
- [Quellen und Prüfgrenzen](quellen.md)
