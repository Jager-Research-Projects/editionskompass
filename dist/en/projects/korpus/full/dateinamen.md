# File Names for Rätselhaft!

Our book files are called `rk_<jahr>_<buch-id>.xml`, for example `rk_1786_b0001.xml`.

- `rk`: corpus shortcuts.
- `jahr`: four digits or `undatiert`.
- `buch-id`: `b` and four digits; stable book identifier.
- `.xml`: single file extension.

## Uniform and platform compatible

For book files and project folders we use ASCII lowercase, digits, underscore and hyphen. No spaces, umlauts or colons, no reserved Windows device names and no names differentiated only by case. Paths remain short and relative. The established metafiles README.md, LICENSE, CITATION.cff and CHANGELOG.md retain their default spelling.

Full title, source and dating are in the TEI metadata. A short file name does not replace this description. The year in the name is checked against the metadata when recording. Data release and selection are recorded for the examination.

## Filtering with Python

```python
from pathlib import Path
files = sorted(Path("data/tei").glob("rk_1786_*.xml"))
```

This allows you to select correspondingly named books of the year 1786. Undated books are selected with `rk_undatiert_*.xml`.

## Amendments and verification

The rule is documented before the first recording in docs/dateinamen.md. Book identification given and retained on recording. If the date is corrected, specifically rename the file in Git, record the assignment and reason in CHANGELOG. Check other references; do not execute renamings casually.

Name patterns, uniqueness even without case-sensitive and double book identifiers are checked with each amendment proposal. The small name examiner only needs Python standard library:

```text
python dateinamen-pruefen.py data/tei
```

It checks filenames, no XML content. schema, references, metadata and technical quality are additionally checked.
