from fastapi import FastAPI
from app.schemas.request import LogInput
from app.schemas.response import DiagnosticOutput

app = FastAPI(
    title="LogMind API",
    description= "API de diagnóstico automatico de logs usando LLM",
    version="0.1.0"
    )

@app.post("/diagnose", response_model=DiagnosticOutput)
def diagnose_log(log_input: LogInput):
    """
    endpoint de diagnóstico de logs
    """
    return  DiagnosticOutput(
        status="success",
        error_type="ConnectionError",
        summary=f"Analisado log de {log_input.source}: {log_input.log_content[:50]}...",
        confidence=0.85,
       affected_components=["database", "airflow"]
    )