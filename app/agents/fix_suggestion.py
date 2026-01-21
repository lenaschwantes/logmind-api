from openai import OpenAI
from app.core.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def suggest_fix(error_type: str, summary: str, log_content: str, source: str) -> dict:
    """
    agent that receives diagnostic and suggests solution
    """
    
    prompt = f"""You are a senior data engineer providing actionable fixes for {source} issues.

DIAGNOSTIC INFO:
- Error Type: {error_type}
- Summary: {summary}
- Original Log: {log_content}

Provide a practical fix suggestion that includes:
1. Immediate action to take
2. Root cause to investigate
3. Prevention strategy

Return JSON with:
- suggested_fix: clear, actionable steps (2-3 sentences max)
- fix_confidence: float 0.0-1.0 (how confident this will work)

Be specific and technical."""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a data engineering solutions expert. Always respond with valid JSON only."},
            {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"},
        temperature=0.3
    )
    
    import json
    return json.loads(response.choices[0].message.content)