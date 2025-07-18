from typing import List, Dict
from backend.services import prompt_modifier
import time

async def generate_frs(urs_content: List[Dict[str, str]], enhanced_prompt: str, options: dict) -> dict:
    """
    Generate FRS items from URS content, ensuring traceability and clear formatting.
    For each URS item, use the LLM to rewrite the description in system implementation style.
    Returns a dict with sections and items.
    """
    items = []
    for idx, req in enumerate(urs_content, start=1):
        # Prepare the LLM prompt for this URS item
        llm_prompt = (
            "Rewrite the following user requirement as a Functional Requirement Specification (FRS) statement from a system implementation perspective. "
            "Be concise, use 'The system shall...' phrasing, and focus on what the system will do to fulfill the requirement.\n\n"
            f"URS: {req['description']}\nFRS:"
        )
        # Call the LLM via prompt_modifier
        frs_description = await prompt_modifier.enhance_prompt(llm_prompt, [], options)
        items.append({
            "id": f"FRS-{idx:04}",
            "description": frs_description,
            "source": req["id"]
        })
        time.sleep(1)  # Add delay to avoid 429 errors
    return {
        "sections": [
            {
                "title": "Functional Requirements",
                "items": items
            }
        ]
    }