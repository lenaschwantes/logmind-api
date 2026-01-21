from fastapi import FastAPI, HTTPException
from app.schemas.request import LogInput
from app.schemas.response import DiagnosticOutput
from app.agents.diagnostic import diagnose_log


app = FastAPI(
    title="LogMind API",
    description="API de diagnóstico automático de logs usando LLM",
    version="0.1.0"
)


@app.post("/diagnose", response_model=DiagnosticOutput)
def diagnose_log_endpoint(log_input: LogInput):
    """
    Endpoint de diagnóstico de logs usando LLM
    """
    try:
        # Chama o agent de diagnóstico
        result = diagnose_log(
            log_content=log_input.log_content,
            source=log_input.source
        )
        
        # Retorna resultado estruturado
        return DiagnosticOutput(
            status="success",
            error_type=result.get("error_type", "Unknown"),
            summary=result.get("summary", "No summary available"),
            confidence=result.get("confidence", 0.5),
            affected_components=result.get("affected_components", [])
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing log: {str(e)}"
        )