from __future__ import annotations

import argparse
import json
from pathlib import Path

from portfolio_tools.catalog_builder import build_catalog, render_markdown_summary


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build machine-readable and Markdown portfolio catalogs."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Repository root that contains course directories.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Destination directory for catalog.json and catalog.md. Defaults to <root>/portfolio.",
    )
    args = parser.parse_args()

    repo_root = args.root.resolve()
    output_dir = (args.output_dir or (repo_root / "portfolio")).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    catalog = build_catalog(repo_root)
    (output_dir / "catalog.json").write_text(json.dumps(catalog, indent=2))
    (output_dir / "catalog.md").write_text(render_markdown_summary(catalog))


if __name__ == "__main__":
    main()
