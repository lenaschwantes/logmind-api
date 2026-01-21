from fastapi import FastAPI, HTTPException
from app.schemas.request import LogInput
from app.schemas.response import DiagnosticOutput
from app.agents.diagnostic import diagnose_log
from app.agents.fix_suggestion import suggest_fix


app = FastAPI(
    title="LogMind API",
    description="Automated log diagnostic API using multi-agent LLM architecture",
    version="0.1.0"
)


@app.post("/diagnose", response_model=DiagnosticOutput)
def diagnose_log_endpoint(log_input: LogInput):
    """
    Multi-agent log diagnostic endpoint
    
    Chain: Diagnostic Agent → Fix Suggestion Agent
    """
    try:
        diagnostic_result = diagnose_log(
            log_content=log_input.log_content,
            source=log_input.source
        )
        
        fix_result = suggest_fix(
            error_type=diagnostic_result.get("error_type", "Unknown"),
            summary=diagnostic_result.get("summary", ""),
            log_content=log_input.log_content,
            source=log_input.source
        )
        
        return DiagnosticOutput(
            status="success",
            error_type=diagnostic_result.get("error_type", "Unknown"),
            summary=diagnostic_result.get("summary", "No summary available"),
            confidence=diagnostic_result.get("confidence", 0.5),
            affected_components=diagnostic_result.get("affected_components", []),
            suggested_fix=fix_result.get("suggested_fix", "No fix suggestion available")
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing log: {str(e)}"
        )