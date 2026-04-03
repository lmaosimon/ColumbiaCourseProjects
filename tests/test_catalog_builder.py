import tempfile
import unittest
from pathlib import Path

from portfolio_tools.catalog_builder import build_catalog, render_markdown_summary


class CatalogBuilderTest(unittest.TestCase):
    def test_build_catalog_groups_visible_course_artifacts(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "HUDK 4050").mkdir()
            (root / "HUDK 4050" / "analysis.ipynb").write_text("{}")
            (root / "HUDK 4050" / "analysis.html").write_text("<html></html>")
            (root / "HUDK 4050" / "reflection.pdf").write_text("pdf")
            (root / "HUDK 4050" / ".ipynb_checkpoints").mkdir()
            (root / "HUDK 4050" / ".ipynb_checkpoints" / "checkpoint.ipynb").write_text("{}")
            (root / "HUDK 4050" / ".artifact.icloud").write_text("skip")

            (root / "HUDM 5122").mkdir()
            (root / "HUDM 5122" / "report.docx").write_text("doc")

            catalog = build_catalog(root)

            self.assertEqual(2, catalog["overview"]["course_count"])
            self.assertEqual(1, catalog["overview"]["notebook_count"])
            hudk = catalog["courses"][0]
            self.assertEqual("HUDK 4050", hudk["course"])
            self.assertEqual(3, hudk["artifact_count"])

    def test_markdown_summary_includes_overview_and_courses(self):
        catalog = {
            "overview": {
                "course_count": 2,
                "artifact_count": 4,
                "notebook_count": 1,
                "html_count": 1,
                "pdf_count": 1,
                "doc_count": 1,
            },
            "courses": [
                {"course": "HUDK 4050", "artifact_count": 3, "notebooks": 1, "html_exports": 1, "documents": 1},
                {"course": "HUDM 5122", "artifact_count": 1, "notebooks": 0, "html_exports": 0, "documents": 1},
            ],
        }

        markdown = render_markdown_summary(catalog)

        self.assertIn("# Portfolio Catalog", markdown)
        self.assertIn("HUDK 4050", markdown)
        self.assertIn("Course Count", markdown)


if __name__ == "__main__":
    unittest.main()
