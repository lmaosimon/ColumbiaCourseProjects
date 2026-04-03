# Contributing

This repository is maintained as a curated coursework portfolio. Changes should improve discoverability, reproducibility, or documentation without altering the original artifacts unnecessarily.

## Good Contributions

- improve the generated catalog or its tests
- tighten ignore rules for notebook byproducts
- add context that helps readers navigate the portfolio

## Verification

```bash
python3 -m unittest tests/test_catalog_builder.py -v
python3 scripts/build_catalog.py
```
