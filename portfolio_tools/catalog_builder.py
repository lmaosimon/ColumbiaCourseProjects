from __future__ import annotations

from pathlib import Path


IGNORED_PARTS = {".git", ".ipynb_checkpoints"}
IGNORED_SUFFIXES = {".icloud"}
NOTEBOOK_SUFFIXES = {".ipynb"}
HTML_SUFFIXES = {".html"}
DOCUMENT_SUFFIXES = {".pdf", ".docx", ".pptx"}
IGNORED_ROOT_DIRS = {"portfolio", "portfolio_tools", "scripts", "tests"}


def build_catalog(root: Path) -> dict:
    courses = []
    course_dirs = [
        path
        for path in root.iterdir()
        if path.is_dir()
        and not path.name.startswith(".")
        and path.name not in IGNORED_ROOT_DIRS
    ]
    for course_dir in sorted(course_dirs):
        artifacts = []
        notebooks = 0
        html_exports = 0
        documents = 0

        for path in _iter_visible_files(course_dir):
            rel_path = path.relative_to(root)
            artifacts.append(str(rel_path))
            suffix = path.suffix.lower()
            if suffix in NOTEBOOK_SUFFIXES:
                notebooks += 1
            elif suffix in HTML_SUFFIXES:
                html_exports += 1
            elif suffix in DOCUMENT_SUFFIXES:
                documents += 1

        if artifacts:
            courses.append(
                {
                    "course": course_dir.name,
                    "artifact_count": len(artifacts),
                    "notebooks": notebooks,
                    "html_exports": html_exports,
                    "documents": documents,
                    "artifacts": artifacts[:12],
                }
            )

    overview = {
        "course_count": len(courses),
        "artifact_count": sum(course["artifact_count"] for course in courses),
        "notebook_count": sum(course["notebooks"] for course in courses),
        "html_count": sum(course["html_exports"] for course in courses),
        "pdf_count": sum(
            1
            for course in courses
            for artifact in course["artifacts"]
            if artifact.lower().endswith(".pdf")
        ),
        "doc_count": sum(
            1
            for course in courses
            for artifact in course["artifacts"]
            if artifact.lower().endswith((".docx", ".pptx"))
        ),
    }
    return {"overview": overview, "courses": courses}


def render_markdown_summary(catalog: dict) -> str:
    overview = catalog["overview"]
    lines = [
        "# Portfolio Catalog",
        "",
        "| Metric | Value |",
        "| --- | ---: |",
        f"| Course Count | {overview['course_count']} |",
        f"| Artifact Count | {overview['artifact_count']} |",
        f"| Notebook Count | {overview['notebook_count']} |",
        f"| HTML Export Count | {overview['html_count']} |",
        f"| PDF Count | {overview['pdf_count']} |",
        f"| Office Document Count | {overview['doc_count']} |",
        "",
        "| Course | Artifacts | Notebooks | HTML Exports | Documents |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for course in catalog["courses"]:
        lines.append(
            f"| {course['course']} | {course['artifact_count']} | {course['notebooks']} | "
            f"{course['html_exports']} | {course['documents']} |"
        )
    lines.append("")
    return "\n".join(lines)


def _iter_visible_files(course_dir: Path):
    for path in course_dir.rglob("*"):
        if not path.is_file():
            continue
        if any(part in IGNORED_PARTS for part in path.parts):
            continue
        if any(part.startswith(".") and part not in {".gitignore"} for part in path.parts):
            continue
        if path.suffix.lower() in IGNORED_SUFFIXES:
            continue
        yield path
