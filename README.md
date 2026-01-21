# LogMind API

Automated diagnostic API for Airflow logs using multi-agent LLM architecture.

## Problem Statement

Data engineers spend significant time manually debugging Airflow logs. This API automates the diagnostic process by analyzing log content and providing structured insights about errors, their root causes, and suggested fixes.

## Current Status

**Version:** 0.1.0 (MVP)

This is the foundation phase focusing on robust API structure and validation:

- FastAPI application with Pydantic schemas
- Request validation with custom field validators
- Structured diagnostic output model
- Automatic API documentation via Swagger UI

Next phase will integrate LLM agents for actual log analysis.

## Technical Stack

- **Framework:** FastAPI 0.128.0
- **Validation:** Pydantic 2.12.5
- **Server:** Uvicorn 0.40.0
- **Python:** 3.12+

Planned integrations: OpenAI API, LangChain for agent orchestration

## Installation
```bash
# Clone and navigate
git clone [repository-url]
cd logmind-api

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Running the API
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000` with interactive documentation at `/docs`.

## Usage Example
```bash
curl -X POST http://localhost:8000/diagnose \
  -H "Content-Type: application/json" \
  -d '{
    "log_content": "[2025-01-20 14:30:00] ERROR: Connection to Snowflake timed out after 30s",
    "source": "airflow"
  }'
```

Response:
```json
{
  "status": "success",
  "error_type": "ConnectionError",
  "summary": "Analisado log de airflow: [2025-01-20 14:30:00] ERROR: Connection...",
  "confidence": 0.85,
  "affected_components": ["database", "airflow"]
}
```

## Project Structure
```
logmind-api/
├── app/
│   └── schemas/
│       ├── request.py    # Input validation models
│       └── response.py   # Output structure models
├── main.py               # FastAPI application
├── requirements.txt      # Python dependencies
└── README.md
```

## Design Decisions

**Pydantic for Validation**

Input validation happens at the schema level rather than in endpoint logic. This keeps the API code clean and ensures consistent validation across all endpoints.

**Structured Output**

Rather than returning free-form text, responses follow a strict schema. This makes the API easy to integrate with downstream systems and enables type-safe client implementations.

**Separation of Concerns**

Schemas live in dedicated modules, keeping the main application file focused on routing and orchestration logic.

## Roadmap

**Phase 2: LLM Integration**
- Implement diagnostic agent using OpenAI API
- Add fix suggestion agent
- Chain agents for complete analysis workflow

**Phase 3: Production Readiness**
- Add sample Airflow logs for testing
- Implement caching for common errors
- Add confidence scoring logic
- Containerize with Docker

**Phase 4: Advanced Features**
- Historical error database
- Pattern recognition for recurring issues
- Batch processing endpoint

## Development Context

Built as part of a portfolio demonstrating:
- Production-grade API design
- LLM integration patterns for data engineering workflows
- Clean architecture principles in Python