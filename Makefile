.PHONY: catalog install test

catalog:
	python3 scripts/build_catalog.py

install:
	python3 -m pip install -e .

test:
	python3 -m unittest tests/test_catalog_builder.py -v
