from pydantic import BaseModel, Field, field_validator


class LogInput(BaseModel):
    log_content: str = Field(
        ...,
        description="Airflow log content for analysis",
        examples=["[2025-01-20 10:30:45] ERROR: Connection timeout to Snowflake"]
    )
    
    source: str = Field(
        default="airflow",
        description="Log source",
        examples=["airflow", "dbt", "spark"]
    )
    
    @field_validator('log_content')
    def validate_log_length(cls, v):
        if len(v) < 10:
            raise ValueError('Log content must be at least 10 characters long')
        return v