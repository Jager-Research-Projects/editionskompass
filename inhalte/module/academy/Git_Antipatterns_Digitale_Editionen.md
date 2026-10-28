# Antipatterns beim Einsatz von Git in digitalen Editionsprojekten

**Arbeitsfassung eines konzeptionellen Katalogs**  
**Stand:** 19. Oktober 2026  
**Umfang:** 25 Antipatterns

## Begriff und Abgrenzung

Ein **Antipattern** ist eine wiederkehrende, zunächst plausible Lösung für ein reales Problem, die unter bestimmten technischen, fachlichen oder organisatorischen Bedingungen systematische Nachteile gegenüber einer geeigneteren Alternative erzeugt. Der Nutzen kann kurzfristig sichtbar sein, während die Nachteile erst später auftreten. Die Praxis kann als Ergänzung sinnvoll sein, obwohl ihre *exklusive* Verwendung problematisch ist. Nicht jedes Antipattern ist unter allen Umständen zu vermeiden.

Ein **Smell** ist ein beobachtbares Symptom, das auf ein Antipattern hinweist, ohne dieses bereits zu beweisen. Smells können sich auf Daten, Versionsgeschichte, Workflow, Governance oder Analysen beziehen.

### Repository-Kontexte

- **Arbeitsrepository:** unterstützt laufende Bearbeitung, Kollaboration und technische Nachvollziehbarkeit. Vorläufige, experimentelle und zeitweilig ungültige Stände können legitim sein, sofern angemessen geschützt und organisiert.
- **Publikationsrepository:** stellt definierte, qualitätsgeprüfte, langfristig identifizierbare und nachnutzbare Editionsdaten bereit. Die Veröffentlichung interner Arbeitsgeschichte ist nicht selbstverständlich erforderlich.
- **Kombiniertes Repository:** kann beide Funktionen wahrnehmen, wenn die unterschiedlichen Anforderungen durch klare Prozesse, Rollen, Zugriffsregeln und Veröffentlichungsstände erfüllt werden.

Die Repository-Typen beschreiben **Funktionen**, nicht zwingend zwei getrennte technische Repositories.

### Einheitliches Steckbriefformat

Jeder Eintrag enthält: **Kontext · Problem · Lösung · Attraktivität · Konsequenzen · Alternative · Begründung · Smells · Geltungsgrenze**. „Geltungsgrenze“ benennt legitime Ausnahmen und insbesondere die Grenze zwischen ergänzender und exklusiver Nutzung.

## Übersicht

| Kennung | Antipattern | Kontext |
|---|---|---|
| A1 | Die Version im Dateinamen | beide |
| A2 | Der Kopienzoo | vor allem Arbeit |
| A3 | Die Geschichte ohne Vergangenheit | beide |
| B1 | Metadaten auf Wanderschaft | beide |
| B2 | Der Branch als Editionsmodell | beide |
| B3 | Die versteckte Editionsentscheidung | beide |
| B4 | Der verwaiste Editionsstatus | Übergang Arbeit → Publikation |
| C1 | Der unentwirrbare Commit | vor allem Arbeit |
| C2 | Die nichtssagende Versionsgeschichte | vor allem Arbeit |
| C3 | Die aufgeschobene Integration | Arbeit |
| C4 | Der Formatierungs-Tsunami | vor allem Arbeit |
| C5 | Der ungeprüfte Publikationsstand | Publikation |
| C6 | Die bewegliche Publikationsfassung | Publikation |
| D1 | Der ewige Zugang | beide |
| D2 | Die vergessene Git-Vergangenheit | vor allem Publikation |
| D3 | Git ist unser Backup | beide |
| D4 | Das herrenlose Repository | beide |
| E1 | Der Commit als Leistungsnachweis | vor allem Arbeit |
| E2 | Das Git als allwissender Zeuge | vor allem Arbeit |
| G1 | Die stillschweigende Git-Vereinbarung | beide |
| G2 | Die pauschale Einwilligung | vor allem Arbeit |
| G3 | Die Zweckwanderung der Git-Daten | Arbeit |
| G4 | Die ungeklärte Rechtekette | beide |
| G5 | Die Lizenz per Knopfdruck | Publikation |
| G6 | Die unbegrenzte Arbeitschronik | vor allem Arbeit |

---

## A. Traditionelle Antipatterns digitaler Editionsarbeit

### A1. Die Version im Dateinamen

- **Kontext:** Arbeits- und Publikationsumgebung.
- **Problem:** Bearbeitungsstände einer Datei müssen erhalten und voneinander unterschieden werden.
- **Lösung:** Jede Fassung wird als separate Datei abgelegt; Versionsnummern, Datums- und Personenzusätze stehen im Namen.
- **Attraktivität:** Einfach, unmittelbar verständlich und ohne spezielle Infrastruktur umsetzbar.
- **Konsequenzen:** Unklare Reihenfolge und Autorität der Fassungen; Änderungen zwischen ihnen sind nicht systematisch dokumentiert; Namenskonventionen versagen bei paralleler Arbeit.
- **Alternative:** Versionskontrolle bei stabilen Dateinamen; definierte Exporte mit eindeutigen Versionskennungen.
- **Begründung:** Dateibenennung übernimmt anstelle eines geeigneten Systems die Verwaltung von Änderungsständen und ihren Beziehungen.
- **Smells:** `final_neu.xml`, `final_v3_korrigiert.xml`, `18-11-2010-Enno-Lied-v3-annotiert-Mark.xml`.
- **Geltungsgrenze:** Versionsangaben in *unveränderlichen Publikationsexporten* sind legitim; problematisch ist die Verwendung solcher Dateikopien als ausschließliche Arbeitsversionierung.

### A2. Der Kopienzoo

- **Kontext:** Vor allem Arbeitsumgebung.
- **Problem:** Dateien sollen vor Verlust geschützt und mehreren Personen zugänglich sein.
- **Lösung:** Unabhängig bearbeitete Ordnerkopien liegen auf Rechnern, Datenträgern und Laufwerken und werden informell ausgetauscht.
- **Attraktivität:** Vertraute Abläufe, Offline-Arbeit und vermeintlich zusätzliche Sicherheit.
- **Konsequenzen:** Konkurrierende Stände, übersehene Änderungen, Überschreibungen und aufwendiger Abgleich.
- **Alternative:** Geregelte Synchronisation mit Versionskontrolle sowie davon unabhängige Backups.
- **Begründung:** Unkoordinierte Replikation löst das Problem gemeinsamer Bearbeitung nicht.
- **Smells:** `Edition_backup`, `Edition_neu`, `Edition_Anna` enthalten jeweils abweichende angeblich aktuelle Dateien.
- **Geltungsgrenze:** Kontrollierte Sicherungskopien, Archiv-Snapshots und ausdrücklich unveränderliche Exporte sind sinnvoll.

### A3. Die Geschichte ohne Vergangenheit

- **Kontext:** Beide; besonders relevant für die historische Rekonstruktion editorischer Arbeit.
- **Problem:** Editionsdaten sollen verbessert und publiziert werden.
- **Lösung:** Ältere Bearbeitungsstände werden überschrieben oder nach der Publikation verworfen.
- **Attraktivität:** Geringerer Speicher- und Organisationsaufwand; Konzentration auf das Endprodukt.
- **Konsequenzen:** Entscheidungen, Korrekturen und verworfene Lösungen können später nicht rekonstruiert werden.
- **Alternative:** Versionierung und eine bewusste, rechtlich geprüfte Bewahrungsstrategie für wissenschaftlich relevante Prozessdokumentation.
- **Begründung:** Ein ausschließlich ergebnisbezogener Speicheransatz zerstört möglicherweise notwendige historische Information.
- **Smells:** Nur der publizierte Endstand existiert; frühere Lesarten lassen sich nicht rekonstruieren.
- **Geltungsgrenze:** Nicht jede flüchtige Zwischenfassung ist archivierungswürdig. Ein Publikationsrepository muss nicht die gesamte interne Arbeitshistorie enthalten.

## B. Git-induzierte editorische Antipatterns

### B1. Metadaten auf Wanderschaft

- **Kontext:** Beide, im Publikationskontext besonders kritisch.
- **Problem:** Fachlich relevante Eigenschaften, Bearbeitungszustände und Zuständigkeiten sollen dokumentiert und abgefragt werden.
- **Lösung:** Sie stehen ausschließlich in Commitnachrichten, Tags, Branches, Issues, Dateinamen oder Ordnern statt in geeigneten strukturierten Metadaten.
- **Attraktivität:** Die Git-Umgebung ist schon vorhanden; der Eintrag erscheint ohne doppelte Pflege möglich.
- **Konsequenzen:** Informationen sind verstreut, nicht einheitlich modelliert und bei separater Bereitstellung der Editionsdaten möglicherweise verloren.
- **Alternative:** TEI-Header (wo passend, etwa `revisionDesc`), fachliche Metadatendateien oder andere geeignete strukturierte Modelle; ergänzende Git-Verweise.
- **Begründung:** Technische Arbeitsorganisation substituiert notwendige fachliche Informationsmodellierung.
- **Smells:** Commitnachrichten dokumentieren Prüfstatus, während fachliche Statusfelder leer bleiben; `/fertig/` ist die einzige Statusquelle.
- **Geltungsgrenze:** Provisorische oder redundante Git-Informationen sind legitim. Zum Antipattern wird die Praxis, wenn dauerhaft benötigte fachliche Angaben *exklusiv* dort verbleiben.

### B2. Der Branch als Editionsmodell

- **Kontext:** Beide.
- **Problem:** Diplomatische, normalisierte oder andere wissenschaftliche Fassungen sollen parallel geführt werden.
- **Lösung:** Ihre fachliche Identität und Beziehung werden ausschließlich durch Branches repräsentiert.
- **Attraktivität:** Git unterstützt parallele Entwicklungszweige direkt.
- **Konsequenzen:** Beziehungen zwischen Fassungen bleiben implizit; ein beweglicher Branchname ist keine stabile wissenschaftliche Fassung.
- **Alternative:** Eigenständige fachliche Repräsentationen und Beziehungen, gegebenenfalls Transformationen; Branches zum Entwickeln, definierte Releases für zitierfähige Stände.
- **Begründung:** Ein technischer Entwicklungsmechanismus ersetzt die Editionstheorie und das Datenmodell.
- **Smells:** Nur Branches `diplomatisch` und `normalisiert` kennzeichnen die Fassungen; keine außerhalb der Branchstruktur lesbare Beschreibung.
- **Geltungsgrenze:** Auch langfristig gepflegte Fassungsbranches sind vertretbar, solange ihre wissenschaftliche Bedeutung ausdrücklich dokumentiert wird.

### B3. Die versteckte Editionsentscheidung

- **Kontext:** Beide.
- **Problem:** Textkritische Entscheidungen sollen begründet und nachvollziehbar sein.
- **Lösung:** Die einzige Begründung steht in Commitnachrichten, Issues oder Pull-Request-Diskussionen.
- **Attraktivität:** Diskussion und Implementierung bleiben unmittelbar verbunden.
- **Konsequenzen:** Begründungen sind beim Export oder bei der Lektüre der Edition nicht zugänglich; wissenschaftliche Entscheidungen hängen an der Arbeitsplattform.
- **Alternative:** Publikationsrelevante Begründungen in Apparat, Kommentar oder Editionsdokumentation überführen; Git-Diskussionen ergänzend verknüpfen.
- **Begründung:** Technische Kommunikation substituiert die fachliche Darstellung der Entscheidung.
- **Smells:** `Lesart B statt A wegen Handschrift X` erscheint nur im Commit.
- **Geltungsgrenze:** Nicht jede Arbeitsdiskussion muss publiziert werden; relevant ist die notwendige Begründung der veröffentlichten Edition.

### B4. Der verwaiste Editionsstatus

- **Kontext:** Übergang Arbeits- zu Publikationsfunktion.
- **Problem:** Ein Bearbeitungsstand muss auf Publikationsreife geprüft werden.
- **Lösung:** Ein operativer Status (geschlossenes Issue, gemergter Branch, `done` im Board) gilt automatisch als fachliche Freigabe.
- **Attraktivität:** Einfacher Workflow und keine doppelte Statusführung.
- **Konsequenzen:** Freigabekriterien bleiben unausgesprochen; unvollständige oder nicht geprüfte Daten können publiziert werden.
- **Alternative:** Expliziter, nachvollziehbarer Freigabeprozess mit definierten Prüfbedingungen und dokumentiertem Ergebnis.
- **Begründung:** Arbeitsorganisation und fachliche Qualitätsentscheidung werden ohne Begründung gleichgesetzt.
- **Smells:** Merge bedeutet automatisch „ediert und geprüft“; keine getrennten Freigabekriterien.
- **Geltungsgrenze:** Ein Projektboard kann die Freigabe abbilden, wenn der Status tatsächlich an überprüfbare Kriterien und Verantwortlichkeiten gebunden ist.

## C. Git-spezifische Workflow-Antipatterns

### C1. Der unentwirrbare Commit

- **Kontext:** Vor allem Arbeitsrepository.
- **Problem:** Viele Änderungen müssen versioniert werden.
- **Lösung:** Sachlich unabhängige Eingriffe werden ohne erkennbare gemeinsame Einheit in einem Commit zusammengefasst.
- **Attraktivität:** Schnelles Committen nach längeren Arbeitsphasen.
- **Konsequenzen:** Schwer prüfbare, schwer erklärbare und nur mühsam selektiv rücknehmbare Änderungen.
- **Alternative:** Logisch zusammengehörige Änderungsgruppen; gesonderte dokumentierte Massenoperationen.
- **Begründung:** Nicht der Umfang, sondern die fehlende fachliche Kohärenz beeinträchtigt die Historie.
- **Smells:** `Alles aktualisiert` verändert Transkription, Kommentar, Software und Konfiguration ohne Zusammenhang.
- **Geltungsgrenze:** Ein großer, sachlich zusammenhängender Datenimport ist legitim und gerade in Publikationsrepositories typisch.

### C2. Die nichtssagende Versionsgeschichte

- **Kontext:** Vor allem Arbeitsrepository.
- **Problem:** Änderungen sollen ohne Zeitverlust festgehalten werden.
- **Lösung:** Nachrichten enthalten keinen hinreichenden Hinweis auf Gegenstand oder Zweck des Commits.
- **Attraktivität:** Niedrige Einstiegshürde; die eigentlichen Änderungen sind im Diff sichtbar.
- **Konsequenzen:** Erhöhte Kosten für Suche, Verständnis und spätere Rekonstruktion.
- **Alternative:** Kurze, aussagekräftige Nachrichten nach einer nachvollziehbaren Konvention.
- **Begründung:** Die vorhandene Dokumentationsfunktion wird ohne entsprechenden Nutzen entwertet.
- **Smells:** Wiederholt `fix`, `asdf`, `nochmal`, `update` bei komplexen Änderungen.
- **Geltungsgrenze:** Kurze oder automatisch erzeugte Commitnachrichten sind nicht an sich problematisch, wenn ihr Zweck ausreichend erkennbar bleibt.

### C3. Die aufgeschobene Integration

- **Kontext:** Arbeitsrepository.
- **Problem:** Mitarbeitende sollen unabhängig arbeiten.
- **Lösung:** Gemeinsam relevante Änderungen bleiben über lange Zeit in getrennten Branches und werden erst spät abgeglichen.
- **Attraktivität:** Kurzfristig wenige Konflikte; maximale Autonomie.
- **Konsequenzen:** Divergenz, Integrationsaufwand und verspätet erkannte Widersprüche.
- **Alternative:** Regelmäßiger Abgleich und Integration entsprechend den tatsächlichen Abhängigkeiten der Arbeitspakete.
- **Begründung:** Kurzfristig vermiedene Koordinationsarbeit wird auf später verschoben und wächst möglicherweise an.
- **Smells:** `anna` und `mark` weichen über Jahre stark von `main` ab; Merges werden wegen Konflikten vermieden.
- **Geltungsgrenze:** Langfristig getrennte Branches sind legitim, wenn Aufgaben unabhängig sind oder die Trennung bewusst begründet wird.

### C4. Der Formatierungs-Tsunami

- **Kontext:** Vor allem Arbeitsrepository.
- **Problem:** XML soll lesbar und konsistent formatiert sein.
- **Lösung:** Editoren ändern bei fachlich kleinen Eingriffen großflächig Einrückungen, Whitespace oder Zeilenumbrüche.
- **Attraktivität:** Lokale Lesbarkeit und automatische Standardisierung.
- **Konsequenzen:** Fachlich relevante Diffs sind verdeckt; `blame` wird weniger aussagekräftig; Konflikte nehmen zu.
- **Alternative:** Einheitliche, stabile Editor- und Formatierungskonventionen; reine Formatierungsänderungen getrennt committen.
- **Begründung:** Nichtinhaltliche Änderungen beeinträchtigen die wichtigste Dokumentationsfunktion des Arbeitsrepos.
- **Smells:** Eine Wortkorrektur produziert Hunderte geänderte Zeilen.
- **Geltungsgrenze:** Gezielte Formatmigrationen sind legitim; im Publikationsrepository kann die detaillierte Zeilenhistorie weniger wichtig sein.

### C5. Der ungeprüfte Publikationsstand

- **Kontext:** Publikationsrepository.
- **Problem:** Neue Editionsergebnisse sollen zügig verfügbar werden.
- **Lösung:** Neue Arbeitsstände werden ohne definierte Qualitätsprüfung direkt als Publikationsstand bereitgestellt.
- **Attraktivität:** Automatisierbare, schnelle Bereitstellung.
- **Konsequenzen:** Ungültige, inkonsistente oder unfertige Daten erhalten einen publizierten Status.
- **Alternative:** Validierung, projektspezifische Tests und explizite Publikationsfreigabe.
- **Begründung:** Ein technischer Commit oder Merge ersetzt die Qualitätsentscheidung.
- **Smells:** Jeder Push auf `main` veröffentlicht ungeprüfte TEI-Dateien; bekannte Validierungsfehler sind öffentlich.
- **Geltungsgrenze:** Öffentlich sichtbare *experimentelle* Arbeitsstände dürfen unfertig sein, wenn ihr Status eindeutig ist; direkte Commits auf `main` sind nicht selbst das Problem.

### C6. Die bewegliche Publikationsfassung

- **Kontext:** Publikationsrepository.
- **Problem:** Eine fortlaufend aktualisierte Edition soll zugleich zitierbar sein.
- **Lösung:** Nur die veränderliche Spitze eines Branches, etwa `main`, ist als veröffentlichte Fassung benannt.
- **Attraktivität:** Es gibt nur eine aktuelle URL und keinen zusätzlichen Release-Aufwand.
- **Konsequenzen:** Historische zitierte Stände sind schwer zu bestimmen; Reproduzierbarkeit leidet.
- **Alternative:** Unveränderliche, eindeutig identifizierte Releases und wo geeignet persistente Identifikatoren; zusätzlich ein `latest`-Zugang.
- **Begründung:** Eine bewegliche Referenz übernimmt exklusiv die Funktion einer stabilen Publikationsfassung.
- **Smells:** Publikationen verweisen nur auf `/tree/main`; es gibt keine dokumentierten Versionen.
- **Geltungsgrenze:** Eine stets aktuelle Fassung ist nützlich, solange frühere Publikationsstände ebenfalls eindeutig referenzierbar sind.

## D. Organisation und Sicherheit

### D1. Der ewige Zugang

- **Kontext:** Beide; im privaten Arbeitsrepo vor allem Lese-, im Publikationsrepo besonders Schreib- und Adminrechte.
- **Problem:** Mitarbeitende benötigen Zugriffsrechte für ihre Aufgaben.
- **Lösung:** Berechtigungen werden beim Einstieg vergeben, aber bei Aufgabenwechsel oder Ausscheiden nicht überprüft oder entzogen.
- **Attraktivität:** Wenig laufender Verwaltungsaufwand; mögliche spätere Mitarbeit bleibt unkompliziert.
- **Konsequenzen:** Unnötige Einsicht oder Änderungskompetenzen; unklare Verantwortlichkeit; erhöhtes Missbrauchs- und Fehlbedienungsrisiko.
- **Alternative:** Rollenbezogene Vergabe minimal notwendiger Rechte, regelmäßige Rezertifizierung und verbindliches On- und Offboarding, auch für Service-Accounts.
- **Begründung:** Die ursprüngliche Autorisierung wird trotz weggefallenem Zweck unverändert fortgeschrieben.
- **Smells:** Ausgeschiedene Personen haben Schreib- oder Adminrechte; Zugriffslisten werden nie überprüft.
- **Geltungsgrenze:** Eine fortdauernde Mitarbeit kann eine erneute, ausdrücklich begründete Berechtigung rechtfertigen. Entzug verhindert nicht die Nutzung schon angefertigter lokaler Kopien.

### D2. Die vergessene Git-Vergangenheit

- **Kontext:** Besonders beim Öffnen eines Publikationsrepositories.
- **Problem:** Vertrauliche Daten sollen vor Veröffentlichung entfernt werden.
- **Lösung:** Nur der aktuelle Datenstand wird bereinigt, die frühere Git-Historie unverändert mit veröffentlicht.
- **Attraktivität:** Das sichtbare aktuelle XML erscheint sauber; Historie wird nicht als eigenständiger Datenbestand wahrgenommen.
- **Konsequenzen:** Frühere XML-Kommentare, personenbezogene Angaben oder Geheimnisse bleiben rekonstruierbar.
- **Alternative:** Prüfung des *gesamten* freizugebenden Datenbestands einschließlich Historie; gegebenenfalls getrenntes Publikationsrepo.
- **Begründung:** Entfernen aus `HEAD` wird fälschlich als vollständiges Löschen verstanden.
- **Smells:** Frühere Commits enthalten interne XML-Kommentare; bisher private Arbeitsgeschichte wird unverändert öffentlich.
- **Geltungsgrenze:** Zulässige interne Bewahrung kann sinnvoll sein. History-Rewriting allein entfernt bereits verbreitete Kopien nicht zuverlässig.

### D3. Git ist unser Backup

- **Kontext:** Beide.
- **Problem:** Verlust und Beschädigung von Daten sollen verhindert werden.
- **Lösung:** Das vorhandene Git-Repository ersetzt alle unabhängigen Sicherungsverfahren.
- **Attraktivität:** Git hält Versionen vor und wird oft auf mehrere Rechner kopiert.
- **Konsequenzen:** Nicht übertragene Arbeit, verlorene Zugangsdaten oder Ausfälle sämtlicher erreichbarer Kopien können ungesichert bleiben.
- **Alternative:** Dokumentierte, getestete Backup- und Wiederherstellungsstrategie, in der Git eine Komponente sein kann.
- **Begründung:** Versionsverwaltung und vollständige Notfallwiederherstellung decken verschiedene Anforderungen ab.
- **Smells:** „Wir haben GitHub, also brauchen wir kein Backup“; keine Restore-Tests.
- **Geltungsgrenze:** Git kann einen wesentlichen Teil einer robusten Sicherungsstrategie bilden.

### D4. Das herrenlose Repository

- **Kontext:** Beide.
- **Problem:** Eine langfristige Infrastruktur benötigt technischen Betrieb und fachliche Verantwortung.
- **Lösung:** Administration, Rechteklärung und Entscheidungen bleiben informell an einzelnen Personen hängen, ohne geregelte Vertretung oder Übergabe.
- **Attraktivität:** Direkte Kommunikation und geringer Formalisierungsaufwand.
- **Konsequenzen:** Verlust von Zugängen, fehlende Nachfolge, unklare Veröffentlichungs- und Sicherheitsentscheidungen.
- **Alternative:** Dokumentierte institutionelle, fachliche, technische und datenschutzbezogene Verantwortlichkeiten sowie Vertretungs- und Übergaberegeln.
- **Begründung:** Eine dauerhaft erforderliche Infrastruktur hängt von ungesicherter persönlicher Verfügbarkeit ab.
- **Smells:** Privater Account als einziger Owner; niemand kennt Regeln bei Ausscheiden des Administrators.
- **Geltungsgrenze:** Einzelpersonen dürfen zuständig sein; die Verantwortung muss jedoch übertragbar und angemessen abgesichert sein.

## E. Antipatterns der Git-Analyse

### E1. Der Commit als Leistungsnachweis

- **Kontext:** Vor allem Arbeitsrepository.
- **Problem:** Arbeitsfortschritt und individuelle Leistung sollen eingeschätzt werden.
- **Lösung:** Commitanzahl, geänderte Zeilen und Frequenz werden unmittelbar als Leistung oder Produktivität gedeutet.
- **Attraktivität:** Leicht verfügbare, quantitativ scheinbar objektive Indikatoren.
- **Konsequenzen:** Verzerrte Vergleiche, Fehlanreize und ungerechte Beurteilungen unterschiedlicher Tätigkeiten.
- **Alternative:** Fachlich begründete, kontextbezogene Kriterien; qualitative Bewertung; zusätzliche Berücksichtigung nicht dokumentierter Arbeit.
- **Begründung:** Technische Aktivität bildet wissenschaftliche Qualität und Leistung nicht unmittelbar ab.
- **Smells:** Mitarbeiterrankings nach Commitzahl; `lines added` wird als Fortschrittsmaß verwendet.
- **Geltungsgrenze:** Als deskriptive Projektmetrik sind solche Zahlen nützlich; ob ihre *personenbezogene Verarbeitung* erlaubt ist, ist zusätzlich gesondert zu klären (G3).

### E2. Das Git als allwissender Zeuge

- **Kontext:** Vor allem Arbeitsrepository.
- **Problem:** Der Editionsprozess soll rekonstruiert werden.
- **Lösung:** Die Git-Historie wird als vollständige Aufzeichnung wissenschaftlicher Arbeit und Entscheidungsfindung behandelt.
- **Attraktivität:** Zeitlich geordnete, detaillierte technische Daten mit Autor- und Änderungsangaben.
- **Konsequenzen:** Offline-Arbeit, Anweisungen, Diskussionen und kollaborative Urheberschaft werden ausgeblendet.
- **Alternative:** Git als begrenzte Quelle verwenden und mit weiteren Prozessquellen sowie Kontextwissen verbinden.
- **Begründung:** Ein selektiver technischer Nachweis wird fälschlich mit dem gesamten wissenschaftlichen Prozess gleichgesetzt.
- **Smells:** „In Git sieht man alles“; fehlende Commits gelten als fehlende Arbeit; Commit-Autor gilt automatisch als wissenschaftlich Verantwortlicher.
- **Geltungsgrenze:** Aussagen über *Git-Aktivität selbst* sind selbstverständlich möglich, solange die Reichweite korrekt benannt wird.

## G. Governance, Rechte und Verantwortlichkeiten

### G1. Die stillschweigende Git-Vereinbarung

- **Kontext:** Beide.
- **Problem:** Zusammenarbeit soll ohne umfangreiche Voraborganisation beginnen können.
- **Lösung:** Mit dem Repository-Zugang gelten Rechte, Pflichten und künftige Nutzungen der Arbeitsdaten stillschweigend als geklärt.
- **Attraktivität:** Unbürokratisch; vertraute informelle Projektkultur.
- **Konsequenzen:** Konflikte über Zugriffe, Veröffentlichung, Anerkennung von Beiträgen und zulässige Datennutzung.
- **Alternative:** Verbindliche und verständliche Repository-Regeln; ergänzende rechtlich notwendige Vereinbarungen und Informationen.
- **Begründung:** Informelle Teilnahme ersetzt nicht die wirksame Regelung relevanter Rechte und Schutzinteressen.
- **Smells:** Keine Repository-Richtlinie; Rechtefragen werden mit „das machen wir immer so“ beantwortet.
- **Geltungsgrenze:** Bestehende institutionelle Regelungen können ausreichen; nicht jede Frage erfordert einen separaten individuellen Vertrag.

### G2. Die pauschale Einwilligung

- **Kontext:** Vor allem Arbeitsrepository.
- **Problem:** Personenbezogene Git-Daten sollen für verschiedene Zwecke genutzt werden.
- **Lösung:** Eine umfassende Anfangserklärung wird als Freigabe aller gegenwärtigen und zukünftigen Auswertungen und Veröffentlichungen behandelt.
- **Attraktivität:** Scheinbar einfache einmalige Absicherung.
- **Konsequenzen:** Unklare Zwecke und Reichweite; mögliche Unwirksamkeit einer Einwilligung insbesondere bei Beschäftigungsabhängigkeit.
- **Alternative:** Verarbeitungszwecke, geeignete Rechtsgrundlagen, Informationen und Schutzmaßnahmen je Nutzung klären; wo passend wirksame spezifische Einwilligung.
- **Begründung:** Pauschale Zustimmung substituiert die notwendige rechtliche und organisatorische Prüfung.
- **Smells:** „Mit der Mitarbeit stimmen Sie jeder zukünftigen Auswertung und Veröffentlichung sämtlicher Git-Daten zu“.
- **Geltungsgrenze:** Eine freiwillige, informierte und hinreichend bestimmte Einwilligung kann in geeigneten Konstellationen legitim sein; sie ist nicht die einzige mögliche Rechtsgrundlage.

### G3. Die Zweckwanderung der Git-Daten

- **Kontext:** Arbeitsrepository.
- **Problem:** Projektleitung möchte Arbeitsabläufe und Engpässe verstehen.
- **Lösung:** Zur Versionierung entstandene personenbezogene Daten werden ohne gesonderte Prüfung für Anwesenheitsüberwachung, individuelle Leistungsbeurteilung oder Personalentscheidungen verwendet.
- **Attraktivität:** Daten existieren bereits und lassen sich automatisiert visualisieren.
- **Konsequenzen:** Zweckverschiebung, Vertrauensverlust, mögliche Eingriffe in Rechte Beschäftigter und Fehlinterpretationen.
- **Alternative:** Zweck und Rechtsgrundlage jeder Analyse prüfen; angemessene Zugriffsbeschränkungen, Datenminimierung und gegebenenfalls aggregierte Auswertung.
- **Begründung:** Ein ursprünglich technischer Datenbestand wird ohne hinreichende Rechtfertigung für neue personenbezogene Zwecke eingesetzt.
- **Smells:** Commit-Heatmaps in Personalgesprächen; Git-Logs als Zeitnachweis ohne vorher festgelegte Regeln.
- **Geltungsgrenze:** Projektbezogene Analysen können legitim sein; dies ist unabhängig von der Frage, ob die daraus abgeleitete Metrik methodisch brauchbar ist (E1).

### G4. Die ungeklärte Rechtekette

- **Kontext:** Beide.
- **Problem:** Gemeinschaftlich erstellte Forschungsdaten sollen bearbeitet, veröffentlicht, lizenziert und archiviert werden.
- **Lösung:** Die Möglichkeit, Beiträge in ein gemeinsames Repository zu committen, gilt als hinreichende Berechtigung für alle späteren Nutzungen.
- **Attraktivität:** Keine Verzögerung durch Rechteklärung.
- **Konsequenzen:** Unklarheit über zulässige Bearbeitung, Verbreitung, Lizenzierung und Archivierung einzelner Werkteile.
- **Alternative:** Schutzstatus, Rechtsinhaber und notwendige Nutzungsbefugnisse für unterschiedliche Beitragsarten frühzeitig klären und dokumentieren.
- **Begründung:** Technische Zugangsberechtigung wird mit urheber- und nutzungsrechtlicher Berechtigung gleichgesetzt.
- **Smells:** Keine Rechteübersicht für Kommentare, Übersetzungen, Digitalisate und Software; Projekt vergibt Lizenzen ohne bekannte Rechtslage.
- **Geltungsgrenze:** Nicht jeder Beitrag ist urheberrechtlich geschützt; Rechte können bereits durch Verträge oder andere Regelungen geklärt sein. Anwendbares Recht ist maßgeblich.

### G5. Die Lizenz per Knopfdruck

- **Kontext:** Publikationsrepository.
- **Problem:** Die Edition soll möglichst offen nachnutzbar sein.
- **Lösung:** Eine einzige Lizenzdatei wird undifferenziert für TEI, wissenschaftliche Texte, Software, Übersetzungen und Fremdmaterial eingesetzt.
- **Attraktivität:** Schnelle und scheinbar eindeutige Open-Science-Kennzeichnung.
- **Konsequenzen:** Falsche Rechteversprechen; möglicherweise unzulässige Lizenzierung fremder Ressourcen.
- **Alternative:** Klare, ressourcenspezifische Lizenz- und Rechteinformationen; einheitliche Lizenz nur bei tatsächlich einheitlicher Rechtslage.
- **Begründung:** Unterschiedliche Nutzungsrechte werden durch einen technischen Einheitsvermerk überschrieben.
- **Smells:** Ein `LICENSE` gilt angeblich für externe Digitalisate und selbst entwickelte Software gleichermaßen, ohne Differenzierung.
- **Geltungsgrenze:** Eine einheitliche Lizenz ist sinnvoll, wenn sie tatsächlich alle betroffenen Ressourcen wirksam abdeckt.

### G6. Die unbegrenzte Arbeitschronik

- **Kontext:** Vor allem Arbeitsrepository und dessen Archivierung.
- **Problem:** Der editorische Entstehungsprozess soll langfristig als Forschungsquelle erhalten bleiben.
- **Lösung:** Vollständige personenbezogene Git-Historien werden ohne definierte Zwecke, Fristen, Zugriffsregeln oder Schutzmaßnahmen dauerhaft bewahrt.
- **Attraktivität:** Maximale Vollständigkeit und keine vorschnelle Vernichtung potenziell relevanter Prozessdaten.
- **Konsequenzen:** Langfristige Rekonstruierbarkeit personenbezogener Arbeitsprofile und interner Kommunikation ohne angemessene Schutzgrundlage.
- **Alternative:** Begründetes Aufbewahrungs- und Archivierungskonzept mit differenziertem Zugang, Schutzmaßnahmen und Berücksichtigung wissenschaftlicher wie persönlicher Interessen.
- **Begründung:** Technische Speicherbarkeit wird mit der Berechtigung zu unbeschränkter Aufbewahrung verwechselt.
- **Smells:** „Alles für immer archivieren“ ohne Regelungen; historische Personendaten sind unbegrenzt zugänglich.
- **Geltungsgrenze:** Wissenschaftliche Langzeitarchivierung kann zulässig und sinnvoll sein, verlangt aber geeignete rechtliche und organisatorische Rahmenbedingungen.

---

## Ergänzende Governance-Checkliste für Editionsrepositories

Eine Repository-Vereinbarung oder ein entsprechend verzahntes Regelwerk sollte mindestens abdecken:

1. Zweck und Funktion des Repositories (Arbeits- und/oder Publikationsfunktion).
2. Institutionelle, fachliche, technische und datenschutzbezogene Verantwortung.
3. Rollen, Zugriffsrechte und Berechtigungsprüfung bei Eintritt, Wechsel und Ausscheiden.
4. Rechte und Pflichten von Mitarbeitenden und externen Beteiligten.
5. Kategorien personenbezogener Daten, Verarbeitungszwecke, Rechtsgrundlagen und Zugriffsregeln.
6. Grenzen von Git-Auswertungen, insbesondere individueller Leistungs- und Arbeitszeitkontrolle.
7. Wissenschaftliche Zuschreibung sowie Urheber- und Nutzungsrechte für unterschiedliche Beitragsarten.
8. Regeln für Publikation, Freigabe, Versionierung, Lizenzierung und Weitergabe.
9. Aufbewahrung, Archivierung, Löschung und Schutz historischer Daten.
10. Verfahren bei Projektende, Personalwechsel, technischen Ausfällen und Sicherheitsvorfällen.

**Wichtig:** Eine Vereinbarung allein schafft nicht automatisch die Rechtsgrundlage für jede gewünschte Datenverarbeitung oder Lizenzierung. Die konkrete Umsetzung muss mit den zuständigen Stellen und dem anwendbaren Recht abgestimmt werden.

## Bewertungsprinzipien für die Anwendung des Katalogs

1. **Lösungscharakter prüfen:** Welches reale Problem will die Praxis lösen, und warum erscheint sie attraktiv?
2. **Repository-Funktion bestimmen:** Handelt es sich um vorläufige Arbeit, eine Veröffentlichung oder beides?
3. **Nachteil konkretisieren:** Welche fachlichen, technischen, sozialen oder rechtlichen Folgen ergeben sich?
4. **Alternative vergleichen:** Welche andere Praxis oder ergänzende Lösung erfüllt die Anforderung besser?
5. **Exklusivität prüfen:** Ist die Praxis nur dann problematisch, wenn eine zusätzliche fachliche Dokumentation fehlt?
6. **Smells nicht überdehnen:** Ein beobachtbares Symptom ist ein Anlass zur Prüfung, kein automatischer Befund.

Die Hauptunterscheidung lautet: Eine fehlerfrei funktionierende Git-Infrastruktur kann fachlich unangemessen eingesetzt oder institutionell unzureichend geregelt sein. Der verantwortbare Einsatz von Git in Editionen ist deshalb zugleich ein **technisches, editorisches und organisatorisch-rechtliches** Problem.

## Herkunft und Status

Dieser Katalog konsolidiert die gemeinsam entwickelten Arbeitsdefinitionen und Steckbriefe aus der vorliegenden Diskussion. Er ist eine **konzeptionelle Typologie, keine empirische Häufigkeitsstudie**. Er knüpft an die hochgeladenen Materialien *skript.pdf* und *folien.pdf* an, insbesondere die Unterscheidung von Arbeits- und Publikationsrepositories sowie die Diskussion von Versionsgeschichte, editorischer Transparenz, Datenschutz und Zugriffsrechten. Die allgemeinen rechtlichen Hinweise sind keine Rechtsberatung.
