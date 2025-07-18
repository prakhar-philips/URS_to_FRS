import os
import requests

async def enhance_prompt(user_prompt, urs_content, options):
    """
    Enhance the user prompt using the first few URS items, or use the user_prompt directly if urs_content is empty.
    If Together.ai API key is set, use Mistral-7B-Instruct model for enrichment via /v1/chat/completions. Else, use string logic.
    """
    api_key = os.getenv("TOGETHER_API_KEY")
    if not api_key:
        return "[LLM API NOT CONFIGURED]"

    # If urs_content is empty, use user_prompt directly (for per-URS FRS generation)
    if not urs_content:
        base_prompt = user_prompt
    else:
        urs_summary = "\n".join(req["description"] for req in urs_content[:5])  # First 5 as sample
        base_prompt = (
            f"Project Overview: {user_prompt}\n"
            f"Primary Requirements (sample):\n{urs_summary}"
        )

    url = "https://api.together.xyz/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "mistralai/Mistral-7B-Instruct-v0.2",
        "messages": [
            {"role": "user", "content": base_prompt}
        ],
        "max_tokens": 256
    }
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()
        return data['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"[LLM API ERROR: {e}]"
