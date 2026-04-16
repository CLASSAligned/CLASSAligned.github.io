#!/usr/bin/env python3
"""Generate _publications/*.md from the ADMI26 BibTeX file and local PDF paths."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
# Optional: pip install bibtexparser -t .vendor-bib
for _vendor in (ROOT / ".vendor-bib",):
    if _vendor.is_dir():
        sys.path.insert(0, str(_vendor))
        break

try:
    import bibtexparser  # noqa: E402
except ImportError as e:
    raise SystemExit(
        "Missing dependency bibtexparser. Install with: pip install bibtexparser\n"
        "Or: pip install bibtexparser -t .vendor-bib"
    ) from e

BIB_PATH = ROOT / "files" / "CLASS AlignED – ADMI26.bib"
PUBLICATIONS_DIR = ROOT / "_publications"
PAPERS_ROOT = ROOT / "files" / "papers"
SITE = "https://CLASSAligned.github.io"

MONTH_MAP = {
    "jan": "01",
    "feb": "02",
    "mar": "03",
    "apr": "04",
    "may": "05",
    "jun": "06",
    "jul": "07",
    "aug": "08",
    "sep": "09",
    "oct": "10",
    "nov": "11",
    "dec": "12",
}


def latex_to_plain(s: str) -> str:
    if not s:
        return ""
    s = str(s).strip()
    for _ in range(20):
        ns = re.sub(r"\{([^{}]*)\}", r"\1", s)
        if ns == s:
            break
        s = ns
    return s.replace("--", "–").strip()


def month_to_mm(month_raw: str | None) -> str:
    if not month_raw:
        return "01"
    m = str(month_raw).strip().strip("{}").lower()[:3]
    if m in MONTH_MAP:
        return MONTH_MAP[m]
    if str(month_raw).strip().isdigit():
        v = int(str(month_raw).strip())
        if 1 <= v <= 12:
            return f"{v:02d}"
    return "01"


def extract_pdf_from_file_field(file_val: str | None) -> tuple[str, str] | None:
    if not file_val:
        return None
    s = str(file_val)
    m = re.search(r"files/(\d+)/(.+?):application/pdf", s)
    if not m:
        return None
    return m.group(1), m.group(2).strip()


def build_paper_url(entry: dict) -> str | None:
    ff = entry.get("file")
    if isinstance(ff, list):
        ff = " ".join(str(x) for x in ff)
    r = extract_pdf_from_file_field(str(ff) if ff else "")
    if r:
        folder, fname = r
        seg = quote(fname, safe="")
        return f"{SITE}/files/papers/{folder}/{seg}"

    url = entry.get("url") or ""
    if isinstance(url, list):
        url = url[0] if url else ""
    url = str(url).strip()
    if url.startswith("http"):
        return url

    doi = entry.get("doi") or ""
    doi = str(doi).strip()
    if doi:
        doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi)
        return f"https://doi.org/{doi}"
    return None


def venue_name(entry: dict) -> str:
    for k in ("journal", "booktitle", "publisher"):
        v = entry.get(k)
        if v:
            return latex_to_plain(str(v))
    return ""


def format_authors_citation(author_raw: str | None) -> str:
    if not author_raw:
        return ""
    parts = re.split(r"\s+and\s+", str(author_raw), flags=re.IGNORECASE)
    names: list[str] = []
    for p in parts[:3]:
        p = latex_to_plain(p.strip())
        if "," in p:
            last, first = p.split(",", 1)
            names.append(f"{first.strip()} {last.strip()}")
        else:
            names.append(p)
    if len(parts) > 3:
        return f"{names[0]} et al."
    return ", ".join(names)


def entry_category(etype: str) -> str:
    et = str(etype).lower()
    if et in ("inproceedings", "incollection"):
        return "conferences"
    return "manuscripts"


def html_escape_text(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build_citation_html(entry: dict) -> str:
    authors_raw = format_authors_citation(entry.get("author")).strip() or "Unknown"
    authors = html_escape_text(authors_raw)
    year_val = entry.get("year")
    try:
        year = str(int(float(str(year_val)))) if year_val else "n.d."
    except (TypeError, ValueError):
        year = str(year_val) if year_val else "n.d."
    title = html_escape_text(latex_to_plain(entry.get("title") or "Untitled"))
    venue = venue_name(entry)
    venue_esc = html_escape_text(venue) if venue else ""
    pages = entry.get("pages")
    pages_s = latex_to_plain(str(pages).strip()) if pages else ""

    cit = f'{authors} ({year}). &quot;{title}.&quot;'
    if venue_esc:
        cit += f" <i>{venue_esc}</i>"
    if pages_s:
        cit += f". {html_escape_text(pages_s)}."
    else:
        cit += "."
    return cit


def yaml_double_quoted(s: str) -> str:
    s = str(s).replace("\\", "\\\\").replace('"', '\\"')
    return f'"{s}"'


def main() -> None:
    with open(BIB_PATH, encoding="utf-8") as f:
        db = bibtexparser.load(f)

    PUBLICATIONS_DIR.mkdir(parents=True, exist_ok=True)

    for entry in db.entries:
        key = entry["ID"]
        etype = entry.get("ENTRYTYPE", "article")

        try:
            yi = int(float(str(entry.get("year")))) if entry.get("year") else None
        except (TypeError, ValueError):
            yi = None
        if not yi:
            yi = 1900
        mm = month_to_mm(entry.get("month"))
        date_str = f"{yi:04d}-{mm}-01"

        paper_url = build_paper_url(entry)
        title_plain = latex_to_plain(entry.get("title") or "Untitled")
        excerpt = title_plain[:280] + ("…" if len(title_plain) > 280 else "")
        venue = venue_name(entry)
        permalink = f"/publication/{date_str}-{key}"
        cat = entry_category(etype)
        citation = build_citation_html(entry)

        lines = [
            "---",
            f"title: {yaml_double_quoted(title_plain)}",
            "collection: publications",
            f"category: {cat}",
            f"permalink: {permalink}",
            f"excerpt: {yaml_double_quoted(excerpt)}",
            f"date: {date_str}",
        ]
        if venue:
            lines.append(f"venue: {yaml_double_quoted(venue)}")
        if paper_url:
            lines.append(f"paperurl: {yaml_double_quoted(paper_url)}")
        lines.append(f"citation: {yaml_double_quoted(citation)}")
        lines.append("---")
        lines.append("")
        lines.append("Full text is available via the link above when provided.")

        ff = entry.get("file")
        r = extract_pdf_from_file_field(str(ff) if ff else "")
        if r:
            folder, fn = r
            pdf_path = PAPERS_ROOT / folder / fn
            if not pdf_path.is_file():
                print(f"WARN: missing PDF {pdf_path}", file=sys.stderr)

        out_path = PUBLICATIONS_DIR / f"{date_str}-{key}.md"
        out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Wrote {len(db.entries)} files to {PUBLICATIONS_DIR}")


if __name__ == "__main__":
    main()
