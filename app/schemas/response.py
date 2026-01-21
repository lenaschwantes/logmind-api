from pydantic import BaseModel, Field
from typing import List


class DiagnosticOutput(BaseModel):
    status: str = Field(
        description="Diagnostic status",
        examples=["success"]
    )
    
    error_type: str = Field(
        description="Error category",
        examples=["ConnectionError"]
    )
    
    summary: str = Field(
        description="Diagnostic summary",
        examples=["Timeout connecting to Snowflake after 30s"]
    )
    
    confidence: float = Field(
        ge=0.0,
        le=1.0,
        description="Diagnostic confidence (0.0 to 1.0)",
        examples=[0.95]
    )
    
    affected_components: List[str] = Field(
        default=[],
        description="Affected components",
        examples=[["database", "airflow_worker"]]
    )
    
    suggested_fix: str = Field(
        description="Suggested solution for the issue",
        examples=["Verify PostgreSQL service is running and check network connectivity"]
    )