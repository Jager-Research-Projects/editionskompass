# Local handover test – executable manual

## 1. Mission and limits

An unknown work computer should be able to perform the demonstration without personal configuration of the previous editor. This is a local sample release. Use no accounts, create no DOI, upload data. For productive archiving, named approvals and institutionally passed accesses apply.

## 2. Environment

Unpack the complete sample package into a fresh folder. Use Python 3 and the lxml version specified in requirements.txt. Document installation path and versions; login data are not included in this manual.

## 3. Execute

In the directory with this README and run_demo.py:

```text
python run_demo.py
```

The run uses only the enclosed files. It checks schema, identifiers and existing references, the source regression test, the two collection as well as the two extractions and creates a sample release.

## Expected results

- Faulty import: four supposed puzzles, no assigned solutions; formal checks passed, source regression failed.
- Corrected import: two puzzles, two correctly referenced solutions; both test levels passed.
- Demo-v1.0: two puzzles among four puzzles = 50 percent.
- Demo-v1.1: eight puzzles among ten puzzles = 80 percent.
- The four original documents continue to yield 50 percent in the new version.
- Only puzzle extraction does not contain "The comb." as a solution. The broader extraction contains the answer.
- probe-release.zip can be opened; all files match the manifested SHA-256 values.

## 5. Error Help

Missing lxml: Check the correct Python environment and requirements.txt. Schema error: Read specific file and error message, do not check. Unexpected numbers: Match data folder and selection with the manifest. Missing file in package: Re-create package and verify completeness; a list does not replace actual files.

## 6. Human surrender test

Another person performs the steps without a call and records unclear points. Only actual steps, environment and result are confirmed. The attached automatic reconstruction has already been checked; an independent human transfer test is still to be carried out.

## 7. Responsibilities after funding

In the fictitious project Miriam is responsible for scientific profile and care commitments; Jonas and a designated representative perform the technical tasks, Tessa advises on archiving and metadata. Institutional ownership/contact roles are confirmed before Lea leaves. Technical access is not an indefinite personal care promise. New contributions are assessed according to the conservation care commitment.
