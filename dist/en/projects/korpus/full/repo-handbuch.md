# Rätselhaft! – Structure and maintenance of the publication repositorys

Patterns for the project · October 22, 2026. The previews are excerpts explaining the respective content and process.

## README.md

The front door: What is the corpus and how do I start an investigation?

### For whom and in what tone?

New users, students and researchers. Write short, inviting and action-oriented; explain technical terms, link them to details.

### When do you plan?

With the publication concept. Set the first task of a new user.

### When?

When the publication repositorys is established, before the first data release.

### When and how to update?

Each time you change the entry, folder, call, license, quote or contact in the same pull request. Before each release, let another person perform the entry.

### What can be automated?

Check relative links and example call automatically. A text change is technically counterread; README is not generated solely from commit messages.

### Minimum content

- Purpose and scope of the corpus
- Relevant data folder and current releases
- First download, call and expected result
- Links to markup, license and citation
- Contact, contributions and care commitment

### Example section

```text
# Rätselhaft! – TEI-Korpus

Für Korpusanalysen verwenden Sie data/tei dieses Releases.
Eine XML-Datei entspricht einem Buch oder einer Sammlung.

## Erste Untersuchung
Kleines Beispiel: examples/nutzungsstart/
Aufruf: python examples/nutzungsstart/untersuchen.py
Erwartet: drei Rätsel und drei zugeordnete Lösungen.

Auszeichnung: docs/auszeichnung.md
Dateinamen: docs/dateinamen.md
Zitation: CITATION.cff · Nutzungsrechte: LICENSE
Fehler mit Release und Rätselkennung als Issue melden.
Nach Projektende: wichtige Korrekturen, neue Aufnahmen nach Kapazität.
```

## LICENSE

Determines the conditions under which the components may be reused.

### For whom and in what tone?

All after-users. Accept license texts unchanged; explain the scope of application in addition to it clearly and without own legal descriptions.

### When do you plan?

When selecting sources: Terms of use record and clarify which license applies to which project components.

### When?

Before the first public approval after completion of the rights clearance.

### When and how to update?

Check the scope of application for new sources or other licensed components. Release changes professionally and explain them in the release notes; do not replace existing license texts casually.

### What can be automated?

A check checks whether LICENSE is present and whether new sources have legal information. The decision on rights of use will not be automated.

### Minimum content

- Name and full text of the selected license
- Clear scope for data, documentation and code
- Source/rights notices and clear exceptions
- References from README and source documentation

### Example section

```text
Aufbau der Datei nach Rechteklärung:

1. Geltungsbereich: Welche Daten oder Werkzeuge?
2. Name und vollständiger Originaltext der gewählten Lizenz
3. Verweis auf Quellen-/Rechtehinweise

Unterschiedliche Lizenzen für Daten und Code werden ausdrücklich
getrennt zugeordnet. Eine Liste von Lizenznamen allein reicht nicht.
```

## CITATION.cff

Provides structured information about citation of the data publication.

### For whom and in what tone?

Researchers and Citation Tools. Precise bibliographic metadata; no advertising language. A short quote in README completes the file.

### When do you plan?

With the publication concept: define title, responsible person and version reference.

### When?

Create before the first release and validate with a CFF test tool.

### When and how to update?

Update each release version and date; enter the confirmed version identifier after archiving. Check authorships for relevant posts. Match all metadata in the release process.

### What can be automated?

Check CFF syntax and required information. Title, version and date can be pre-stocked from a common release source; consciously confirm authorship and archive proof.

### Minimum content

- CFF version and message to quote
- Title and resource type
- Persons responsible by name, if applicable ORCID
- Data version and date of publication
- Confirmed identifiers and reference address

### Example section

```text
cff-version: 1.2.0
message: "Bitte zitieren Sie die verwendete Datenversion."
type: dataset
title: "Rätselhaft! – TEI-Korpus"
authors:
  - family-names: Berger
    given-names: Lea
version: 1.0.0
date-released: 2026-10-22
# Weitere Verantwortliche und bestätigten Versionsnachweis ergänzen.
# Versions-DOI nach bestätigter Archivierung eintragen.
```

## CHANGELOG.md

Explains what has changed for users between two datasets.

### For whom and in what tone?

Researchers who repeat results or use a new release. Name inventory and meaning changes; no unfiltered commit list.

### When do you plan?

Along with version schema and release path.

### When?

With the first public version. Ongoing changes initially under "Unpublished" collect.

### When and how to update?

Each pull request with usable data/model change adds an entry. Before the release, arrange entries, set date and version; identify known errors of affected older versions.

### What can be automated?

Templates and notes collected from pull requests save work. The editors check their scientific statement; a raw Git log edition is not a changelog.

### Minimum content

- Version and date
- New or removed collection
- Corrections and affected identifiers
- Model/markup Changes with Effects
- Known borders and, where appropriate, migration information

### Example section

```text
# Änderungen

## Unveröffentlicht
- Reimannotation wird als zusätzliche Schicht vorbereitet.

## 1.1.0 – Beispielrelease
- Ergänzt: neue Sammlung b0003.
- Korrigiert: Lösungszuordnungen in b0001, IDs unverändert.
- Auswirkung: Auswertungen mit Lösungen bitte erneut prüfen.

## 1.0.0 – Erster geprüfter Bestand
- Umfang und bekannte Grenzen im Release beschrieben.
```

## data/

Contains the relevant published data; raw take-overs and study copies do not belong to it as competing versions.

### For whom and in what tone?

People and programs. Predictable structure and machine-readable metadata; explanatory prose in README or docs.

### When do you plan?

Before recording the first book files: Set unit, identifiers, metadata and package division.

### When?

With the first partial inventory audited.

### When and how to update?

Check new or corrected data about pull requests and release them professionally. Only a release makes the audited overall status the designated research basis.

### What can be automated?

Check name patterns, ID clarity, XML/schema, references and inventory. Technical recording and approval remain a separate step.

### Minimum content

- Unique corpus folder tei/
- One book/collection file per unit
- Documented IDs, Origin and Dating
- No casual exports or private working copies

### Example section

```text
data/
└── tei/
    ├── rk_1786_b0001.xml
    ├── rk_1820_b0003.xml
    └── rk_undatiert_b0004.xml

Jede Kennung gehört zu genau einer Buch-/Sammlungsdatei.
Für Studien werden Releases und Auswahlregeln festgehalten.
```

## data/tei/

Keeps the book files available in the same documented TEI markup.

### For whom and in what tone?

Corpus researchers and programs. Same structures mean the same throughout the collection; automatic additional annotation is offered separately.

### When do you plan?

Set unit and TEI model before the first major conversions.

### When?

For the first checked book file; document borderline cases immediately.

### When and how to update?

Compare before/after inventory for conversions. Version model changes together with schema, documentation and migration notice.

### What can be automated?

Check schema and references for changes. Check year and book identifier in the file name against the relevant metadata.

### Minimum content

- Source description and book identification
- Puzzle identifiers and verse/text structure
- Solutions with unique assignment
- Explicit labelling of uncertainties
- Uniform filename pattern

### Example section

```text
rk_1786_b0001.xml
rk_1820_b0003.xml
rk_undatiert_b0004.xml

Schnellauswahl der Beispieldatierung 1786:
data/tei/rk_1786_*.xml

Auswahl für die Untersuchung zusammen mit dem Release dokumentieren.
```

## rk_1786_b0001.xml

A complete book or collection file; file name and stable identifier connect storage and metadata.

### For whom and in what tone?

Expert reading and automated procedures. TEI structure follows the model; clearly identify uncertainties in metadata.

### When do you plan?

Identifier given during recording. Name rule applies already at the first file.

### When?

After collection of the source and assignment of the book identification.

### When and how to update?

Corrections in the same file path can be made intelligibly. Changes in dating, specifically rename and explain assignment in the changelog; the stable book identifier is retained.

### What can be automated?

A name checker can find rules violations and double book IDs. Changes to titles or interpretation do not always need new file names.

### Minimum content

- corpus abbreviation rk
- Four-digit year indication or undated
- Stable book identification b0001
- File extension .xml
- Compliance with documented metadata

### Example section

```text
rk_1786_b0001.xml
│  │    └── stabile Buchkennung
│  └─────── dokumentiertes Erscheinungsjahr
└────────── Korpuskürzel

Metadaten enthalten den vollständigen Titel, Quelle und Datierung.
Der Dateiname ist ein kurzer, einheitlicher Einstieg für Filter.
```

## schematic/

Published the rules according to which the corpus stock is technically tested.

### For whom and in what tone?

Editing and technical after-users. Explain rules with small marginal case examples; describe technical meaning in docs.

### When do you plan?

With the TEI model and before a large automated recording.

### When?

As soon as the first data model can be tested.

### When and how to update?

Each model change changes schema, affected data, tests and documentation in the same modification proposal. Keep schema version in release.

### What can be automated?

Schema generation and data validation are automatic. Tests must check both valid and deliberately invalid cases.

### Minimum content

- Project adaptation of the TEI model
- Executable schema and other test rules
- Instructions for production and execution
- Link to markup documentation

### Example section

```text
schema/
├── korpus.odd
├── korpus.rng
└── README.md

ODD: dokumentierte TEI-Anpassung.
RNG: daraus erzeugte Strukturprüfung.
README: Erzeugung, Abhängigkeiten und Prüfaufruf.
```

## docs/

Keeps the binding project rules and explains technical decisions.

### For whom and in what tone?

New contributors and external researchers. Explain terms, formulate rules in a concise manner and prove them with correct examples.

### When do you plan?

In the conceptual phase, define structure and responsibility for rules.

### When?

With the first model and the first working rules; not write down at the end of the project.

### When and how to update?

When changing rules together with data, schema or tools. Apply technical decisions from issues to the permanent documentation. Check contradictions before releases.

### What can be automated?

Check links and examples; a pull request form asks for affected documentation sites. Content will be reread professionally.

### Minimum content

- Publication concept and scope
- TEI markup with examples
- IDs, filenames and metadata
- Check/approval and release process
- Contact, contributions and care

### Example section

```text
docs/
├── publikationskonzept.md
├── auszeichnung.md
├── dateinamen.md
└── releaseablauf.md

Aus dateinamen.md:
Eine Buchdatei heißt rk_<jahr>_<buch-id>.xml.
Jahr: vier Ziffern oder undatiert. Buch-ID: b plus vier Ziffern.
Die Zuordnung wird bei Aufnahme und Release geprüft.
```

## examples/

Allows a small complete examination without personal introduction.

### For whom and in what tone?

New users, courses and follow-up projects. Step by step guidance, few dependencies and expected output instead of mere script collection.

### When do you plan?

With the first usage scenario: What task should someone create in a few steps?

### When?

Before the first public release with a small matching data section.

### When and how to update?

When changing data model, call or dependencies, customize example and guide in the same pull request. Just run before each release; occasionally let a new person try it out.

### What can be automated?

Execute the example in a fresh environment and compare results. An additional human entry test checks comprehensibility.

### Minimum content

- Small, fully usable sample data
- Short guide with call
- Script/Notebook including dependencies
- Expected expenditure
- Data and tool covers

### Example section

```text
examples/
└── nutzungsstart/
    ├── README.md
    ├── korpus.xml
    ├── untersuchen.py
    └── ausgabe/
        └── ergebnis.json

Aufruf aus dem Repository-Hauptordner:
python examples/nutzungsstart/untersuchen.py
Erwartet: 3 Rätsel, 3 Lösungen und getrennte Exporte.
```

## tests/

Makes known errors automatically recognisable and describes the test scope.

### For whom and in what tone?

Editing and technical responsible persons. Name test cases with expectation and professional reason; use small manageable test data.

### When do you plan?

Together with conversion and model: What must a processing step not lose?

### When?

On the first import and on the first tool. Each found error complements a test case.

### When and how to update?

For data/model/tool changes, check expectations professionally. Not only rewrite a failed test appropriately; clear the cause. Run complete test run before release.

### What can be automated?

Automatically execute each pull request. The report specifies verified properties; the technical source control and approval are additionally recorded.

### Minimum content

- Test call and dependencies
- Valid and selectively invalid cases
- IDs, references and content retention
- File Name/Metadata Check
- Regression tests for known errors

### Example section

```text
tests/
├── README.md
├── pruefe_dateinamen.py
├── pruefe_verweise.py
└── fixtures/
    ├── mit-loesungen.xml
    └── ohne-loesungen-fehler.xml

Erwartung: zwei Rätsel UND zwei zugeordnete Lösungen.
Ein reiner XML-Test würde den Verlust nicht erkennen.
```
