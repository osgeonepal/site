import os
import re
from datetime import datetime
from pathlib import Path

from google.oauth2 import service_account
from googleapiclient.discovery import build

# --------------------------------------------------
# CONFIG
# --------------------------------------------------

DOC_ID = os.environ.get("GOOGLE_DOC_ID")

BASE_DIR = Path("docs/Meetings")
BASE_DIR.mkdir(parents=True, exist_ok=True)

SCOPES = ["https://www.googleapis.com/auth/documents.readonly"]

MONTHS = {
    "January": 1, "February": 2, "March": 3, "April": 4,
    "May": 5, "June": 6, "July": 7, "August": 8,
    "September": 9, "October": 10, "November": 11, "December": 12,
}

DATE_PATTERN = re.compile(
    r"(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2}),\s+(\d{4})"
)

# --------------------------------------------------
# AUTH
# --------------------------------------------------

def get_service():
    creds = service_account.Credentials.from_service_account_info(
        eval(os.environ["GOOGLE_CREDENTIALS"]),
        scopes=SCOPES
    )
    return build("docs", "v1", credentials=creds)

# --------------------------------------------------
# PRESERVE MARKDOWN FORMAT (BOLD + BULLETS + STRUCTURE)
# --------------------------------------------------

def extract_markdown(doc):
    md = ""

    for block in doc.get("body", {}).get("content", []):
        para = block.get("paragraph")
        if not para:
            continue

        line = ""
        is_bullet = para.get("bullet") is not None

        for el in para.get("elements", []):
            run = el.get("textRun")
            if not run:
                continue

            text = run.get("content", "")
            style = run.get("textStyle", {})

            # preserve bold
            if style.get("bold"):
                text = f"**{text.strip()}** "

            line += text

        line = line.rstrip()

        if not line.strip():
            md += "\n"
            continue

        if is_bullet:
            md += f"- {line.strip()}\n"
        else:
            md += f"{line.strip()}\n"

    return md

# --------------------------------------------------
# SPLIT BY H3 DATES
# --------------------------------------------------

def format_paragraph(para):
    """Helper to convert a single GDoc paragraph to Markdown."""
    line = ""
    is_bullet = para.get("bullet") is not None
    p_style = para.get("paragraphStyle", {})
    named_style = p_style.get("namedStyleType")
    should_bold_heading = named_style in {"TITLE", "HEADING_1", "HEADING_4"}
    
    # Process text elements (bold, etc.)
    for el in para.get("elements", []):
        run = el.get("textRun")
        if not run:
            continue
        text = run.get("content", "")
        style = run.get("textStyle", {})
        if style.get("bold"):
            text = f"**{text.strip()}** "
        line += text
    
    line = line.strip()
    if not line:
        return ""
    
    # Apply bullet if present
    if is_bullet:
        return f"- {line}"
    if should_bold_heading and not (line.startswith("**") and line.endswith("**")):
        return f"**{line}**"
    return line

def split_meetings(doc):
    body = doc.get("body", {}).get("content", [])
    meetings = []
    current_date = None
    current_lines = []

    for block in body:
        para = block.get("paragraph")
        if not para:
            continue
            
        # Use our new helper to get formatted text
        formatted_line = format_paragraph(para)
        
        # Check for H3 for splitting
        p_style = para.get("paragraphStyle", {})
        is_h3 = p_style.get("namedStyleType") == "HEADING_3"
        match = DATE_PATTERN.search(formatted_line)

        # START OF NEW MEETING
        if is_h3 and match:
            if current_date and current_lines:
                meetings.append((current_date, "\n\n".join(current_lines)))

            month, day, year = match.group(1), int(match.group(2)), int(match.group(3))
            current_date = datetime(year, MONTHS[month], day)
            current_lines = [formatted_line]
        else:
            if current_date:
                current_lines.append(formatted_line)

    if current_date and current_lines:
        meetings.append((current_date, "\n\n".join(current_lines)))

    output = []
    for date_obj, block in meetings:
        filename = f"meeting_{date_obj.strftime('%Y-%m-%d')}.md"
        output.append((date_obj, filename, block))
    return output

# --------------------------------------------------
# SAVE FILES
# --------------------------------------------------

def save(meetings):
    created = []
    skipped = []

    for date_obj, filename, block in meetings:

        year_dir = BASE_DIR / str(date_obj.year)
        year_dir.mkdir(parents=True, exist_ok=True)

        path = year_dir / filename

        if path.exists():
            skipped.append(str(path))
            continue

        title = f"# OSGeo Nepal General Meeting - {date_obj.strftime('%B %d, %Y')}\n\n"

        content = title + block.strip() + "\n"

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        created.append(str(path))

    return created, skipped

# --------------------------------------------------
# MAIN
# --------------------------------------------------

def main():
    if not DOC_ID:
        raise ValueError("Missing GOOGLE_DOC_ID")

    service = get_service()
    doc = service.documents().get(documentId=DOC_ID).execute()

    meetings = split_meetings(doc)

    created, skipped = save(meetings)

    print("\n=== SYNC COMPLETE ===")
    print("Created:", len(created))
    print("Skipped:", len(skipped))


if __name__ == "__main__":
    main()
