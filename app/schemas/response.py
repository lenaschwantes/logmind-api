from pydantic import BaseModel, Field
from typing import List

class DiagnosticOutput(BaseModel):
    status: str = Field(
        descriptopm="status",
        examples=["success"]
    )

    error_type: str = Field(
        description="categoria do erro",
        examples=["ConnectionError"]
    )
    summary: str=Field(
        description="resumo do diagnóstico",
        examples=["timeout na conexão com snowflake apos 30s"]
    )
  
    confidence: float = Field(
        ge=0.0,
        le=1.0,
        description="confiança do diagnóstico (0.0 a 1.0)",
        examples=[0.95]
    )
    affected_components: List[str] = Field(
        default=[],
        description="componentes afetados",
        examples=[["database", "airflow_worker"]]
    )