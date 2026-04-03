# Learning Analytics Portfolio

This repository curates graduate-level learning analytics, educational data mining, and research methods work into a reproducible portfolio. It preserves the original course artifacts while adding a modern index, artifact cataloging, and lightweight repository hygiene so the work reads as a research portfolio rather than an unstructured class dump.

## What Is Inside

- `HUDK 4050` and `HUDK 4051`: notebook-heavy analytics, modeling, and recommendation-system exercises
- `HUDK 4054`, `HUDK 5053`, `HUDM 4125`, `HUDM 5026`, `HUDM 5122`, `ITSF 5035`: capstones, reflections, reports, and applied research deliverables
- [`portfolio/catalog.md`](./portfolio/catalog.md): generated inventory of course artifacts
- [`scripts/build_catalog.py`](./scripts/build_catalog.py): reproducible catalog generator for the repository

## Portfolio Snapshot

The generated catalog currently indexes:

- 8 course directories
- 137 tracked artifacts
- 18 notebooks
- 29 HTML exports

## Repository Workflow

Install the lightweight portfolio tooling:

```bash
python3 -m pip install -e .
```

Generate the portfolio catalog:

```bash
build-learning-catalog --root .
```

Run the catalog tests:

```bash
python3 -m unittest tests/test_catalog_builder.py -v
```

## Professionalization Pass

This modernization layer adds:

- a machine-readable and human-readable artifact catalog
- notebook hygiene rules for iCloud placeholders and checkpoint files
- a clearer top-level narrative for reviewers, recruiters, and collaborators

The original coursework remains intact; the repository now presents it with a structure suitable for public review.
