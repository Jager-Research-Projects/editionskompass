# Anna: Chancen und Risiken – ausführliche Redaktion

Stand: 20. Oktober 2026 · Prototyp 0.3 / Grammatik 0.5.0

Basiszustand, qualitative Einschätzungen für fünf Jahre. Zustandsabhängige Änderungen werden in der Webansicht ergänzt.

## Unterstützung

ID: P01-C01

**mittel / mittel**

Es wäre sehr erfreulich, wenn Anna Mitstreiter:innen für ihr Projekt findet – vielleicht auch jemanden, der den Kommentar sorgfältig gegenliest. Vier Augen sehen mehr als zwei! Mira könnte eine Parallelstelle kennen, jemand anderes Fehler in den Verweisen entdecken. Passende Expertise ist denkbar; vor einer konkreten Zusage bleiben Mitwirkung und fachlicher Gewinn offen.

**Wie hilft Git?** Anna kann über den Hostingdienst weitere Personen einladen und Änderungen nachvollziehen. Mira kann einen Abschnitt lesen und Hinweise schicken oder mit passendem Zugriff selbst Änderungen vorschlagen. Ein Pull-/Merge-Request bündelt einen Vorschlag samt Diskussion; Anna kann ihn prüfen, überarbeiten lassen und gezielt übernehmen. Die verfügbaren Rollen hängen vom jeweiligen Dienst ab.

**Was gibt es zu bedenken?** Sollen alle Beteiligten alle Arbeitsdaten samt erreichbarer Geschichte lesen können? Ein eigener Bearbeitungszweig versteckt keine Dateien. Für einen begrenzten Auftrag kann ein bereinigter Ausschnitt genügen. Lesen oder auch Schreiben? Hinweise per Mail, als Issue oder als Änderungsvorschlag? Wer entscheidet über die Übernahme? Fachliche Beiträge werden nach vereinbarten Regeln etwa im TEI-Header (respStmt) und Änderungsverzeichnis (revisionDesc/change) gewürdigt. Commitmetadaten helfen bei der Zuordnung, ersetzen diese Attribution und die Erklärung der Verantwortung aber nicht.

**Handlung:** Zugang für Mitwirkende passend einrichten, zunächst gegebenenfalls nur lesend. Einen verständlichen Reviewausschnitt, Rückkanal, Integrationsverantwortung und Form der Anerkennung vereinbaren.

**Zuständig:** Anna und mögliche Mitwirkende

[TEI: Verantwortungsangaben](https://tei-c.org/release/doc/tei-p5-doc/en/html/ref-respStmt.html) · [TEI: Änderungsverzeichnis](https://tei-c.org/release/doc/tei-p5-doc/en/html/ref-revisionDesc.html)

## Revision

ID: P01-C02

**mittel / hoch**

Ein Jahr nach der Veröffentlichung entdeckt Anna eine überzeugendere Lesart. Für eine zweite Buchauflage wäre das bei diesem kleinen Thema vielleicht zu wenig. Ihre digitale Edition kann sie trotzdem fachlich revidieren und erneut freigeben. Der mögliche Gewinn ist groß; welche neuen Erkenntnisse tatsächlich auftauchen, weiß sie noch nicht.

**Wie hilft Git?** Anna vergleicht die frühere und die überarbeitete Datei und dokumentiert die Änderungen. Wichtige Zwischenstände kann sie mit Git-Tags markieren: Ein Tag ist ein Name für einen bestimmten gespeicherten Stand, etwa „seminar-2026“ oder „edition-1.0“. So findet Anna die damalige Fassung gezielt wieder, während sie bereits weiterarbeitet. Eine alternative Deutung kann sie zunächst getrennt ausprobieren und nach Prüfung übernehmen.

**Was gibt es zu bedenken?** Eine Tippfehlerkorrektur ist etwas anderes als eine neue Editionsentscheidung. Was hat sich geändert, warum und wer hat mitgewirkt? Der Editionsbericht muss dies erklären. Ein Tag allein veröffentlicht oder archiviert nichts und ersetzt keine verständliche Versionsangabe oder Zitationsregel. Tags lassen sich technisch ändern oder löschen; veröffentlichte Markierungen behandelt Anna deshalb als fest und vergibt für Revisionen neue Namen. Ältere zitierte Stände bleiben zugänglich oder archiviert. Git aktualisiert weder vorhandene Druckexemplare noch fremde Downloads. Bei paralleler Buchausgabe sollte klar sein, welche digitale Fassung ihr entspricht.

**Handlung:** Eine einfache Versions- und Zitationsregel festlegen. Wichtige Stände mit verständlich benannten, kurz erläuterten Tags markieren und diese ausdrücklich zum Hostingdienst übertragen; ein gewöhnlicher Push überträgt nicht automatisch alle Tags. Öffentliche Tags nur im bereinigten Publikationsrepo setzen. Änderungen begründen, alte Freigabestände erhalten und im nächsten Release auf die Unterschiede zum Buch oder zur früheren Datenfassung hinweisen.

**Zuständig:** Anna; bei Bedarf fachliches Gegenlesen und Publikations-/Archivdienst

[Git: Stände mit Tags markieren](https://git-scm.com/book/de/v2/Git-Grundlagen-Taggen)

## Lehre

ID: P01-C03

**mittel / mittel**

Anna möchte ihren Studierenden zeigen, wie eine Edition entsteht. Eine Passage mit zwei möglichen Lesarten und einem noch nicht fertigen Kommentar wäre lebensnäher als nur die fertige Ausgabe. Das Seminar kann gute Rückfragen und neue Beobachtungen hervorbringen. Ohne konkreten Termin ist diese Möglichkeit zunächst offen.

**Wie hilft Git?** Anna hält die ausgewählte Seminarfassung als eigenen benannten Stand fest. Sie kann genau diesen Ausschnitt für die Gruppe bereitstellen und später zeigen, wie sich der Kommentar verändert hat. Beiträge aus der Lehrveranstaltung lassen sich getrennt sammeln und vor der Aufnahme in die Edition prüfen.

**Was gibt es zu bedenken?** Welche Passagen sind fachlich und hinsichtlich der Rechte vorzeigbar? Wer darf den Ausschnitt erhalten? Ein interner Lehrstand ist keine öffentliche Teilpublikation. Studierende brauchen eine verständliche Einführung und müssen wissen, wie ihre Vorschläge verwendet und gegebenenfalls genannt werden. Commitzahlen und Uhrzeiten sind keine geeigneten Leistungsmaße.

**Handlung:** Lehrfassung, Lesekreis und Rückkanal vorbereiten; Qualitätsstatus kennzeichnen und Übernahme sowie Anerkennung studentischer Beiträge klären.

**Zuständig:** Anna als Lehrende, Studierende und bei Bedarf Lehr-/Infrastrukturunterstützung

## Teilpublikation

ID: P01-C04

**mittel / mittel**

Ein Kapitel ist bereits gut kommentiert, andere Teile brauchen noch Monate. Anna könnte das fertige Kapitel schon nutzbar machen. So bekommen Interessierte einen belastbaren Ausschnitt und können ihr Rückmeldungen geben. Eine angekündigte Freigabe bedeutet allerdings noch nicht, dass jemand sie tatsächlich nutzt.

**Wie hilft Git?** Ein ausgewählter geprüfter Stand wird als Release veröffentlicht. In einem eigenen Publikationsrepo kann Anna nur die freigegebenen TEI-Dateien, Metadaten und Dokumentation bereitstellen. Spätere Ergänzungen werden als weitere nachvollziehbare Stände veröffentlicht; die private Arbeitsgeschichte muss nicht mitkommen.

**Was gibt es zu bedenken?** Was gehört wirklich zum freigegebenen Teil? Funktionieren seine Register-, Bild- und Kommentarverweise auch ohne den Rest? Sind Rechte, Nutzungsbedingungen und Attribution geklärt? Anna kennzeichnet fehlende Teile und bekannte Grenzen. Ein Datenrepo braucht noch keine Website, und ein Webangebot ersetzt die vereinbarte Archivierung nicht.

**Handlung:** Einen selbstständig verständlichen Teilbestand auswählen, Verweise und Rechte prüfen, README und Versionshinweis beilegen und Freigabe sowie Archivübergabe dokumentieren.

**Zuständig:** Anna; bei Bedarf Fachreview, Metadatenberatung und Archivdienst

## Buchpublikation

ID: P01-C08

**ungeklärt / hoch**

Anna stellt sich ihre Edition gern als Buch vor: ein guter Satz, sorgfältiges Lektorat und ein Verlag, der passende Leser:innen erreicht. Eine Verlagsanfrage wäre eine echte Chance. Sie plant aber realistisch mit einer TEI-Datenpublikation und gegebenenfalls einer kleinen Website. Ein konkretes Verlagsinteresse wird im Modell nicht vorausgesetzt.

**Wie hilft Git?** Anna kann dem Verlag einen klar bezeichneten geprüften Stand anbieten. Aus derselben kontrollierten Quelle lassen sich Daten- und Druckfassung ableiten, wenn ein passender Ausgabeweg eingerichtet ist. Sie kann den Stand zur Buchausgabe festhalten und spätere digitale Revisionen davon unterscheiden. Git vermittelt keinen Verlagskontakt und setzt kein Buch von selbst.

**Was gibt es zu bedenken?** Welche Leistungen übernimmt der Verlag, welche Kosten und Zeit entstehen für Anna? Darf die TEI-Fassung einschließlich Kommentar weiter öffentlich bleiben und später revidiert werden? Welche Rechte soll sie einräumen, welche hat sie bereits vergeben oder offen lizenziert? Buchsatz, Bilder und fremde Beiträge können eigene Bedingungen haben. Eine wirksam erteilte CC-Lizenz lässt sich gegenüber den sie einhaltenden Nutzer:innen nicht einfach zurücknehmen; Buch und offene Daten sind dadurch nicht grundsätzlich unvereinbar. Der konkrete Vertrag muss zu den bereits bestehenden und geplanten Veröffentlichungen passen.

**Handlung:** Früh klären, ob offene Daten, Minimalfrontend und spätere Revisionen neben der Buchausgabe möglich bleiben. Leistungen, Kosten, Rechte, Versionszuordnung und Korrekturweg mit dem Verlag konkret vereinbaren; vorhandene Lizenzen offenlegen.

**Zuständig:** Anna und interessierter Verlag; bei Vertrags- und Rechtefragen qualifizierte Beratung

[Creative Commons: Lizenzen wählen](https://creativecommons.org/cc-license-your-work/) · [Creative Commons: ergänzende Vereinbarungen](https://creativecommons.org/faq/)

## Rechnerausfall

ID: P01-R01

**mittel / hoch**

Annas Laptop startet nicht mehr. Das muss nicht das Ende der Editionsarbeit sein: Was sie regelmäßig committet und zum verlässlich betriebenen Uni-GitLab übertragen hat, liegt dort weiterhin samt Git-Geschichte. Gefährdet bleiben letzte lokale Änderungen und Dateien, die sie gar nicht in diesen Sicherungsweg aufgenommen hat.

**Wie hilft Git?** Anna kann auf einem Ersatzrechner eine neue Kopie des Repos anlegen und am zuletzt übertragenen Stand weiterarbeiten. Git zusammen mit dem extern betriebenen Repo bildet für die erfassten Dateien einen wirksamen Sicherungsweg gegen Rechnerverlust. Eine zusätzliche unabhängige Kopie verbessert die Absicherung.

**Was gibt es zu bedenken?** Ein Commit nur auf dem kaputten Rechner ist noch keine externe Kopie. Hat Anna wirklich gepusht? Wie aktuell ist der Stand? Liegen Abbildungen, Notizen, große externe Objekte und benötigte Konfigurationen ebenfalls vor? Anna braucht außerdem ihre neuen Zugangsmöglichkeiten und die passende Arbeitsumgebung. Eine vorhandene Kopie sollte einmal praktisch ausprobiert werden.

**Handlung:** Regelmäßig committen und pushen. Repo probeweise in einen frischen Ordner klonen, ältere Stände sowie Vorschau prüfen und dokumentieren, was gesichert ist. Für weitere Dateien einen ergänzenden Sicherungsweg festlegen.

**Zuständig:** Anna; der Hostingdienst verantwortet seinen vereinbarten Betrieb, direkte Hilfe nur soweit nötig

## Repo-Zugang

ID: P01-R02

**ungeklärt / hoch**

Annas Uni-Anbindung endet, während die Edition noch wächst. Sie möchte weiterarbeiten und fragt sich, ob ihr bisheriger Repo-Zugang bleibt. Ein auslaufendes Konto ist kein Grund, die Daten aufzugeben: Der Arbeitsbestand kann an einen anderen geeigneten Ort mitkommen. Welche Kontoregel gilt, ist zunächst ungeklärt.

**Wie hilft Git?** Eine vollständige lokale Git-Kopie enthält die versionierten Dateien und ihre erreichbare Geschichte. Anna kann sie zu einem neuen privaten Repo übertragen und danach wieder regelmäßig abgleichen. Für ihren kleinen Arbeitsweg genügen in der Regel eine verständliche Anleitung, ein neuer Zugang und ein Test des Ergebnisses.

**Was gibt es zu bedenken?** Vor dem Zugangsende letzte Stände abgleichen und eigene Änderungen festhalten. Sind alle benötigten Branches, Tags und externen Objekte erfasst? Issues, Rechte, Automationen und Webveröffentlichung sind nicht automatisch Bestandteil der Git-Dateien. Der Repo-Umzug beantwortet auch nicht die Fragen nach oXygen-Lizenz und Beratung.

**Handlung:** Kontoregel rechtzeitig klären. Nach der Umzugsanleitung neues Ziel anlegen, Daten und Geschichte übertragen, eine frische Kopie testen und den neuen Arbeitsort dokumentieren.

**Zuständig:** Anna anhand der Anleitung; zuständige Stelle klärt den alten Zugang, technische Hilfe bei Sonderfällen

## Beratung

ID: P01-R03

**ungeklärt / mittel**

Bisher konnte Anna bei einer kniffligen XML-Frage die Beratung an der Universität ansprechen. Nach einem Stellenwechsel ist dieser Kontakt womöglich nicht mehr verfügbar. Ein kleiner Fehler kann dann unverhältnismäßig viel Editionszeit kosten. Ob die Beratung tatsächlich endet oder ein anderes Angebot bleibt, muss sie klären.

**Wie hilft Git?** Versionierte Vorlagen, Schemas und verständliche Betriebsnotizen helfen Anna, bewährte Einstellungen wiederzufinden. Sie kann zeigen, seit welcher Änderung ein Problem auftritt, und ein kleines Beispiel für eine Rückfrage vorbereiten. Ein einfacher Repo-Umzug bleibt mit Anleitung auch ohne direkte Beratung möglich.

**Was gibt es zu bedenken?** Git beantwortet keine fachlichen Modellierungsfragen und wartet keine kaputte Pipeline. Wer hilft bei Problemen, die Anna nicht allein lösen kann? Kann sie Vorschau und Prüfung ohne den alten Server starten? Welche wiederkehrenden Schritte sollten so gut dokumentiert sein, dass sie niemanden dafür braucht?

**Handlung:** Beratungsbedingungen klären, wichtige Routinen mit Beispielen dokumentieren und einen realistischen Ersatzkontakt für Sonderfälle suchen. Den Arbeitsweg so einfach halten, dass laufende Hilfe selten nötig wird.

**Zuständig:** Anna und bisherige bzw. mögliche neue Beratungsstelle

## Werkzeugwechsel

ID: P01-R04

**ungeklärt / mittel**

Anna arbeitet inzwischen gern in oXygen. Nun ist unklar, ob sie die Campusberechtigung nach ihrem Ausscheiden weiter nutzen darf. Die vertraute Oberfläche könnte wegfallen. Ihre TEI-Daten werden dadurch nicht unlesbar, aber der Wechsel von Werkzeug und Arbeitsroutine braucht Aufmerksamkeit.

**Wie hilft Git?** TEI-Dateien, Schema, Vorlagen und Transformationsregeln können weiter versioniert werden. Anna kann ein anderes geeignetes XML-Werkzeug an einer Kopie ausprobieren und die Ergebnisse mit dem bisherigen Stand vergleichen. Die Git-Geschichte ist nicht an oXygen gebunden.

**Was gibt es zu bedenken?** Lizenzberechtigung zuerst klären, statt den Wegfall zu vermuten. Ein Ersatzeditor bietet nicht zwingend dieselbe Author-Ansicht oder dieselben Hilfen. Funktionieren Eingabe, Validierung und Ausgabe noch? Proprietäre Einstellungen können Anpassung brauchen. Für den Markdown-Weg ist diese konkrete oXygen-Abhängigkeit nicht vorausgesetzt.

**Handlung:** Berechtigung prüfen; bei Bedarf einen repräsentativen Abschnitt im alternativen Arbeitsweg bearbeiten, validieren und ausgeben. Unterschiede und nötige Schritte in einer kurzen Anleitung dokumentieren.

**Zuständig:** Anna; Lizenzverwaltung klärt Berechtigung, punktuelle Einrichtungshilfe bei Bedarf

## Vertraulichkeit

ID: P01-R05

**mittel / hoch**

Anna und Mira schreiben beim Gegenlesen kleine XML-Kommentare: Rückfragen, halbfertige Gedanken und auch einmal einen Kalauer. Vor der Veröffentlichung löscht Anna diese Notizen. In der aktuellen Datei sind sie weg – in früheren Git-Ständen können sie weiterhin stehen. Eine ungeprüfte Veröffentlichung des Arbeitsrepos könnte das interne Gespräch mitveröffentlichen.

**Wie hilft Git?** Das private Arbeitsrepo bewahrt Änderungen für die Zusammenarbeit. Ein getrenntes Publikationsrepo kann eine eigene Geschichte ausschließlich geprüfter Freigaben führen. Anna übernimmt dafür bereinigte Dateien ohne die interne Git-Geschichte; ein bloßer Klon oder öffentlich gemachter Arbeitszweig trennt die Historie nicht.

**Was gibt es zu bedenken?** Wer darf die Arbeitsdaten und alten Kommentare lesen? Welche Metadaten, Dateinamen oder Begleitdateien sind ebenfalls intern? Auch ein privates Repo verlangt einen passenden Lesekreis. Ein neuer Commit, der Kommentare löscht, entfernt frühere Inhalte nicht. Bereits verteilte Kopien lassen sich nicht zuverlässig zurückholen. Wissenschaftliche Attribution soll beim Bereinigen erhalten bleiben.

**Handlung:** Vor Aufnahme sensible Inhalte abgrenzen. Für die Veröffentlichung Dateien, Metadaten und erreichbare Historie prüfen; einen bereinigten Export in das separate Publikationsrepo übernehmen und eine frische öffentliche Kopie kontrollieren.

**Zuständig:** Anna und Mira für den internen Umgang; Anna verantwortet die Freigabe

[GitHub: Daten aus einer Repo-Geschichte entfernen](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)

## Fortführung

ID: P01-R06

**ungeklärt / hoch**

Anna will die Edition selbst fertigstellen. Trotzdem ist es beruhigend, wenn nach einer langen Unterbrechung jemand verstehen könnte, was bereits vorliegt. Eine Kopie der Dateien ist hilfreich, aber ihre Entscheidungen, offenen Fragen und der Weg zur Ausgabe müssen ebenfalls nachvollziehbar sein.

**Wie hilft Git?** Ein verfügbarer Repo-Stand mit Geschichte hält die gespeicherte Arbeit zusammen. README, Editionsrichtlinien und ein dokumentierter Freigabestand können mitgeführt werden. Eine benannte Person kann damit den vorhandenen Bestand prüfen, sichern und gegebenenfalls weiterbearbeiten.

**Was gibt es zu bedenken?** Wer wäre tatsächlich bereit und berechtigt, Verantwortung zu übernehmen? Gibt es einen geregelten Zugang, ohne Annas persönliches Passwort weiterzugeben? Sind Lizenzen, offene Aufgaben und benötigte externe Dateien dokumentiert? Git erklärt keine nur im Kopf oder außerhalb des Repos getroffenen Entscheidungen und bestimmt keine Nachfolge.

**Handlung:** Eine zustimmende Kontaktperson oder einen Träger vereinbaren, Zugänge sauber regeln und ein kleines Übergabepaket erstellen. Mit einem Probelauf prüfen, ob eine andere Person daraus eine Ausgabe erzeugen kann.

**Zuständig:** Anna und ausdrücklich vereinbarte Vertretung bzw. aufnehmende Einrichtung

## Zusatzaufwand

ID: P01-R07

**mittel / mittel**

Mira bietet Hilfe an, die Studierenden haben Ideen und nach einer Teilfreigabe kommen weitere Hinweise. Anna freut sich – und stellt fest, dass sie Antworten, Prüfungen und Integration ebenfalls leisten muss. Unterstützung eröffnet Möglichkeiten, erhöht aber zunächst auch den Abstimmungsbedarf.

**Wie hilft Git?** Kleine abgegrenzte Vorschläge, ein nachvollziehbarer Dateivergleich und gesammelte Rückfragen erleichtern die Bearbeitung. Anna kann Vorschläge einzeln prüfen und dokumentiert übernehmen, anstatt mehrere kommentierte Dateien mühsam zusammenzusuchen.

**Was gibt es zu bedenken?** Ein kompliziertes Git-Verfahren könnte eine hilfsbereite Kollegin auch abschrecken. Reicht für diesen Auftrag eine Mail oder ein kommentierter Ausschnitt? Wie viel darf parallel geändert werden? Wer beantwortet Fragen, entscheidet bei Widersprüchen und nennt die Mitwirkenden? Automatische Prüfungen ersetzen die fachliche Durchsicht nicht.

**Handlung:** Einen kleinen Auftrag, einen passenden Rückkanal und einen realistischen Zeitraum vereinbaren. Nicht mehr Beiträge gleichzeitig anstoßen, als Anna nachvollziehbar prüfen kann.

**Zuständig:** Anna und jeweils beteiligte Mitwirkende

## Hostwechsel

ID: P01-R08

**ungeklärt / hoch**

Die Vorschau läuft bisher bequem auf dem Uni-Server. Nach einem Hostwechsel sind die Dateien zwar da, die gewohnte Webausgabe aber nicht. Anna muss herausfinden, welche Verarbeitung auf dem alten Dienst eingerichtet war. Ob ihr Ausgabeweg davon abhängt, ist zu Beginn noch ungeklärt.

**Wie hilft Git?** Transformationsregeln, Prüfskripte und eine Anleitung können gemeinsam mit der Edition versioniert werden. Wenn der Ausgabeweg auch lokal ausführbar ist, kann Anna ihn am neuen Ort wiederverwenden und Ergebnisse vergleichen.

**Was gibt es zu bedenken?** Git überträgt keine Serverzugänge, geheimen Einstellungen oder bereitgestellten Rechenumgebungen von selbst. Ein Dienst wie GitHub Pages erwartet eine statische Website; rohe TEI-Dateien ergeben noch keine fertige Leseansicht. Wer pflegt die Vorlage, und welche Schritte funktionieren ohne den bisherigen Host?

**Handlung:** Mit einem kleinen Beispiel den lokalen Ausgabeweg testen und benötigte Werkzeuge notieren. Beim Wechsel Host-Einstellungen und Webadresse gesondert anpassen; danach Verweise und Ausgabe prüfen.

**Zuständig:** Anna anhand der Betriebsanleitung; Einrichtung und Sonderfälle mit technischer Unterstützung

[GitHub Pages: statische Websites](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)

