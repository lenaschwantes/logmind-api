from openai import OpenAI
from app.core.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def diagnose_log(log_content: str, source: str) -> dict:
    """
    Agent que analisa o log e retorna diagnóstico estruturado
    """
    
    prompt = f"""You are a senior data engineer specializing in debugging {source} logs.

Analyze this log and provide a structured diagnostic:

LOG:
{log_content}

Return a JSON with:
- error_type: category (ConnectionError, SyntaxError, ResourceError, etc)
- summary: brief explanation of what went wrong
- confidence: float between 0.0-1.0 (how confident you are)
- affected_components: list of affected systems/components

Be concise and technical."""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a data engineering diagnostic expert. Always respond with valid JSON only."},
            {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"},
        temperature=0.3
    )
    
    import json
    return json.loads(response.choices[0].message.content)