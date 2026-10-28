# Rätselhaft! – Publication concept 0.4

The GitHub project organization publishes the TEI corpus as a scientific data product. The concept is versioned from the beginning and continued with changes.

## For whom?

Students, corpus researchers and model groups should independently get to a comprehensible investigation from a download.

## What collection?

data/tei contains the relevant book files. Solutions are associated with puzzle identifiers. Automatic annotations are separated and call procedures and test status.

## How to get in?

README explains inventory, license, structure and first call. Small examples, subpackages and complete data can be used locally without a university account.

## How to release?

Exams, inventory comparison and targeted technical reading precedes the release. Tag, release notes and archive package denote the publication.

## How to improve?

Errors are reported as issues, corrections are checked and described in new releases. Older research findings remain referenceable; their defects will not become mandatory for future versions.

## Structure and markup

data/tei contains the relevant book files. Source context, puzzles, boundaries and solutions are documented. The identifiers remain stable; a new model or merging gets an assignment table. Different markup practices are identified. Additional automatic annotations name procedures, tool version, origin and test status. They are selectively selectable and can be omitted.

README, LICENSE, CITATION.cff and CHANGELOG indicate entry, usage rights, citation and changes. schema/ contains the model, docs/ the rules, examples/ the small entry into use and tests/known test cases. Derivative exports refer to input, transformation and version. Tools and additional annotations can have separate repos; concrete references are recorded.

## Technology and infrastructure openness

Full named downloads can be used without Uni access. Large collections are additionally meaningfully portioned; each package division is documented. The first attempt does not require a huge archive. Open formats, relative paths and platform compatible filenames are mandatory. Tested environments are called. The Python example facilitates entry, but does not require Pythons as the only way to process TEI data. A library can use local data; the API is an additional offer.

## Tests and approval

The team checks XML well-formedness, schema, identifiers and references, unexpected inventory changes, derived issues and selected points against the source. Successful analysis does not replace approval. Regression tests ensure known conversion cases. Automatic tests and technical control are documented with their scope. Lea prepares the data; Jonas checks the technical process; Miriam confirms the editorial approval.

## Versions, errors and research

Released stands get tags and releases with inventory, changes and known limits. Archive packages receive matching metadata and a version reference. Data release, selection, extraction and tool stand together form the research proof. In case of errors a new corrected version is published; affected old versions are marked and remain referenceable. A defective folder structure therefore does not have to be continued.

## Contributions and care

README designates contact and issue path. Contributions are checked; extensions can remain connected as separate versioned layers. Limited conservation maintenance applies after sponsoring. Active extensions require capacity. Data and examples also remain usable independently of running services.

## Try practically before each release

A person starts in a fresh environment when downloading, finds the relevant inventory, introduces the example and names data and process level. Gaps flow into README, tests and concept.

## Designation and care

Book files are called rk_<year>_<book-id>.xml. The full name rule is in dateinamen.md. The Repo manual repo-handbuch.md specifies purpose, target group, planning, installation, minimum content and maintenance process for each entry.
