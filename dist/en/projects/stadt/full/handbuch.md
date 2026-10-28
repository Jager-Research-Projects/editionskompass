# Work regulations, manuals and participation rules

## Plausible first folder structure

```text
die-andere-stadt-edition/
├── README.md                 Entry and relevant data
├── CITATION.cff              Quotation information
├── LICENSE                  Conditions of use of the released collection
├── CHANGELOG.md              Changes published
├── CONTRIBUTING.md           Cooperation and examination
├── MAINTAINERS.md            Tasks and responsibilities
├── data/
│   └── ms01/
│       └── eh-ms01-b012r.xml  Technically useful unit
├── schema/                   ODD, schema, additional rules
├── transforms/               Versioned transcription and derivatives
├── import/manifests/          Herkunft, Prüfsummen, Übernahmeprotokolle
├── docs/
│   ├── handbuch.md
│   ├── kennungen.md
│   ├── forschungsstaende.md
│   ├── publikationsstaende.md
│   └── uebergabe.md
└── tests/                    Technical and technical test cases
```

This is the proposed structure of the fictitious edition repos, not the directory of the prototype. Whole convolutes are only placed in a file if they can be edited meaningfully together. The pilot checks conflict frequency and references. Sheet-wise files are an example; the actual cut follows the source context.

Outside are front-end code, autonomous research repos, secured import packages and image services. Manifesto files connect them without uncontrollably multiplying the same collection.

## Manual 1.0: Compulsory workflow in the case of

1. Get the current project status before processing; request support in open conflicts.
2. Edit a corresponding change and check the image or the technical basis.
3. View comparison, perform appropriate testing, secure and transfer change with justification.
4. Release the intended editorial review. An automatic test status alone does not release a read.
5. Edit internal queries in the agreed channel; do not include confidential content and access data in the Git history.

## Manual 1.1: completed after import sample

The TEI file in the Editionsrepo is the main working version of this unit after it has been imported. Re-exports do not replace this file. Later corrections are compared, specifically taken over and checked. The acquisition protocol describes the status of origin, transformation, acceptance and identifiers. The production phase ends after inventory and controlled transfer of remaining units.

## Rules of participation and agreements

Prior to access, the task, permitted data usage, read/write permissions, editorial approval, contribution assignment and protection obligations are recorded. Internal stands and Git history may not be made accessible to unauthorized persons. Local copies on used devices must be protected. Possible unauthorized access, compromised access data or loss of a device with project copies are immediately reported to project management and technical contact.

Before leaving or changing roles, it is agreed which research stands may be used and copied further, which data must be returned or deleted and which documented exceptions apply. Associated further work receives a suitable new role. Own research rights do not justify automatic clearance of the official edition.

The project covers all accessing parties: core team, auxiliary staff, associated research, external technology, publishing house and library. Personal agreements, institutional regulations and service agreements are assigned after task and access. Git evaluations receive a transparently agreed purpose and access circle; personal performance rankings do not belong to the workflow.

The institutional examination of the later agreement and its legal embedding is a separate step. This editorial document describes the intended case and does not yet provide a signed draft contract.
