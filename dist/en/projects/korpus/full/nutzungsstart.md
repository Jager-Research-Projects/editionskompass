# Rätselhaft! – from download to first investigation

Artificial exercise inventory · Demo-0.2 · no historical evidence.

This small package works locally with Python 3.10 or later, without additional packages, API, account or network connection. Unpack files together into a folder. Run in the terminal in this folder:

```
python untersuchen.py
```

Expected: three puzzles, three associated solutions; a rhyme pair puzzle, a verified solution and a saved rhyme word. The program writes `ergebnis.json`, `testeingaben.jsonl` and `loesungen.jsonl` to `ausgabe/`.

## What belongs to where?

- `korpus.xml`: significant TEI sample inventory with stable identifiers. Solutions are stored separately and connected via corresp.
- `untersuchen.py`: Selection, inventory/reference check and two separate exports. No TEI-schema checks. The tests for the other sample collection are in the parent package.
- `ausgabe/testeingaben.jsonl`: Puzzle texts and IDs without solutions. This file can use a model attempt as input.
- `ausgabe/loesungen.jsonl`: separate reference solutions for subsequent evaluation; do not enter the model in the test input.
- `ausgabe/ergebnis.json`: Selection, demo data collection, expected inventory and executed checks.

The texts, identifiers and categories are invented for this exercise. The categories are not mutually exclusive. This miniature corpus is not a scientific benchmark. It illustrates the separation of packages and experiments; it does not execute a language model and evaluates no model performance.

## A seminar task

Compare the third puzzle with a self-created prose version without rhyming. As an edit, record it separately from the original. Formulate a hypothesis and an evaluation rule before the model attempt. What is the meaning of different writings and several plausible answers?

For an actual benchmark: call data release and selection, record model/tool capture and parameters, check training and test inventory including related evidence and document evaluation rules. The complete corpus download should follow the same structure rules as the small start.

## Rights of use

The three puzzle texts and example script newly written for this demonstration can be used in CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/ . Historical data of a real project need its own rights and license clarification.
