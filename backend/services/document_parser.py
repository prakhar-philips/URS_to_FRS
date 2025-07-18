import fitz  # PyMuPDF
import os
import re
import tempfile
from typing import List, Dict

async def parse_urs(urs_file) -> List[Dict[str, str]]:
    """
    Parse the uploaded URS PDF and extract structured requirements.
    Returns a list of dicts: {"id": "SF-01", "description": "..."}
    """
    # Save uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp:
        tmp.write(await urs_file.read())
        temp_file = tmp.name

    requirements = []
    try:
        doc = fitz.open(temp_file)
        all_text = []
        for page in doc:
            page_text = page.get_text()
            # Clean up text: remove extra whitespace, non-text artifacts
            page_text = re.sub(r'\s+', ' ', page_text)
            page_text = re.sub(r'[^\x20-\x7E\n]', '', page_text)  # keep printable chars
            all_text.append(page_text)
        doc.close()
        text = "\n".join(all_text)

        # Improved regex: capture any text after the ID as the requirement description
        req_pattern = re.compile(
            r'((SF|UI|DH|INT|REP|SE|ER|UR)-\d{2,3})\s+(.+?)(?=(SF|UI|DH|INT|REP|SE|ER|UR)-\d{2,3}|$)',
            re.IGNORECASE | re.DOTALL
        )
        for match in req_pattern.finditer(text):
            req_id = match.group(1).strip()
            description = match.group(3).strip()
            requirements.append({
                "id": req_id,
                "description": description
            })
    finally:
        os.remove(temp_file)

    return requirements
