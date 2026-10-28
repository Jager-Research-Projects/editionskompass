# GitHub Pages · Veröffentlichung / deployment

Vorgesehenes Repository: `Jager-Research-Projects/editionskompass`. Betreuung über `ThomasPagina`. Die öffentliche Dateiauswahl, Lizenzen und Anbieterangaben sind freigegeben.

1. Lizenzierung, öffentliche Dateiauswahl sowie DE/EN-Anbieter-, Datenschutz- und Zugänglichkeitsangaben bestätigen und finalisieren.
2. Repository in der Organisation anlegen; die Organisationsberechtigung und Actions-Freigabe prüfen. Für Commits eine mit ThomasPagina verknüpfte verifizierte E-Mail oder die tatsächliche GitHub-noreply-Adresse konfigurieren. Keine Adresse erraten und keine Tokens in Dateien speichern.
3. Den bestätigten Quellstand als ersten öffentlichen Stand auf `main` hochladen. Die gesicherte private Entstehungsgeschichte bleibt getrennt.
4. Unter Settings → Pages die Quelle GitHub Actions wählen. Optional das Environment `github-pages` mit einer manuellen Freigabe versehen.
5. Erst nach inhaltlicher Freigabe `approved` in `publication.json` auf `true` setzen. Der Workflow baut, prüft und übergibt ausschließlich `_site/` an Pages. Pull Requests veröffentlichen nicht.
6. Die tatsächliche Website prüfen: beide Sprachen, direkte Abschnittslinks, Downloads, Quiz, Strategie, DB-Entscheidung und Workshop-Paket. Erst dann Version 1.0.0 markieren und Release-Notizen ergänzen.

Für einen anderen Repository-Namen die Werte `repository` und `base_path` anpassen. Für eine spätere eigene Domain außerdem `origin` und den Exportpfad bewusst umstellen; eine Domain ist derzeit nicht vorgesehen.

## English

Confirm licenses, the public file selection and operator/privacy/accessibility information first. Create the repository with the appropriate organisation permissions, configure commits with an email actually associated with ThomasPagina, and upload the approved initial public source state. Select GitHub Actions in Pages settings. Set `approved` to `true` only after approval; pull requests never deploy. Verify the live site before tagging the first release.

The workflow uses GitHub’s Pages deployment permissions and needs no personal access token in the repository. See https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages .
