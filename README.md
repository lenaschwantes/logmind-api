# LogMind API

Automated diagnostic API for Airflow logs using multi-agent LLM architecture.

## Problem Statement

Data engineers spend significant time manually debugging Airflow logs. This API automates the diagnostic process by analyzing log content through specialized LLM agents that identify errors and suggest actionable fixes.

## Current Status

**Version:** 0.2.0 (Multi-Agent MVP)

Fully functional multi-agent system with sequential processing:

- FastAPI application with Pydantic validation
- Two-stage LLM agent architecture (diagnostic + fix suggestion)
- OpenAI GPT-4o-mini integration
- Structured JSON responses with confidence scoring
- Automatic API documentation via Swagger UI

## Architecture

### Multi-Agent Pipeline
```
Log Input → Agent 1 (Diagnostic) → Agent 2 (Fix Suggestion) → Complete Response
```

**Agent 1: Diagnostic Agent**
- Analyzes log content and identifies error patterns
- Categorizes error types (ConnectionError, SyntaxError, etc)
- Determines affected components
- Provides confidence scoring (0.0-1.0)

**Agent 2: Fix Suggestion Agent**
- Receives diagnostic context from Agent 1
- Generates actionable fix recommendations
- Includes immediate actions and prevention strategies
- Context-aware suggestions based on error type and summary

### Design Rationale

Separation of diagnostic and solution concerns ensures:
- Each agent has focused responsibility
- Better prompt engineering for specific tasks
- Easier testing and iteration
- Modular architecture for future agent additions

## Technical Stack

- **Framework:** FastAPI 0.128.0
- **Validation:** Pydantic 2.12.5
- **LLM:** OpenAI GPT-4o-mini
- **Environment:** python-dotenv
- **Server:** Uvicorn 0.40.0
- **Python:** 3.12+

## Installation
```bash
# Clone repository
git clone [repository-url]
cd logmind-api

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

## Running the API
```bash
uvicorn main:app --reload
```

API available at `http://localhost:8000` with interactive documentation at `/docs`.

## Usage Example

### Request
```bash
curl -X POST http://localhost:8000/diagnose \
  -H "Content-Type: application/json" \
  -d '{
    "log_content": "[2025-01-20] ERROR: psycopg2.OperationalError: could not connect to server: Connection refused",
    "source": "airflow"
  }'
```

### Response
```json
{
  "status": "success",
  "error_type": "ConnectionError",
  "summary": "PostgreSQL connection refused - server may be down or unreachable",
  "confidence": 0.95,
  "affected_components": ["PostgreSQL Database", "Airflow Task"],
  "suggested_fix": "Check if PostgreSQL server is running on the target host. Verify firewall settings allow connections on port 5432."
}
```

## Project Structure
```
logmind-api/
├── app/
│   ├── agents/
│   │   ├── diagnostic.py        # Agent 1: Error diagnosis
│   │   └── fix_suggestion.py    # Agent 2: Solution suggestions
│   ├── core/
│   │   └── config.py            # Configuration and environment variables
│   └── schemas/
│       ├── request.py           # Input validation models
│       └── response.py          # Output structure models
├── main.py                      # FastAPI application and routing
├── .env                         # Environment variables (not in repo)
├── .env.example                 # Environment template
├── requirements.txt             # Python dependencies
└── README.md
```

## Key Technical Decisions

**Multi-Agent Architecture**

Instead of a single monolithic LLM call, the system uses specialized agents. This improves accuracy and allows each agent to be optimized independently through targeted prompt engineering.

**Sequential Processing**

Agent 2 receives Agent 1's output as context. This ensures fix suggestions are directly relevant to the identified error type and root cause, rather than generic troubleshooting steps.

**Structured Outputs**

Using OpenAI's `response_format={"type": "json_object"}` guarantees valid JSON responses, eliminating parsing errors and enabling type-safe client integration.

**Confidence Scoring**

Each diagnostic includes a confidence metric, allowing downstream systems to handle low-confidence results differently (e.g., flagging for human review).

## Performance Characteristics

- **Response time:** 4-6 seconds (2 sequential LLM calls)
- **Token usage:** ~500-800 tokens per request
- **Cost:** ~$0.0002 per diagnostic (GPT-4o-mini pricing)

For production deployment, consider:
- Caching common error patterns
- Parallel processing where agents don't depend on each other
- Response streaming for better UX

## Roadmap

**Phase 3: Production Features**
- Sample Airflow logs collection for testing
- Error pattern caching and recognition
- Batch processing endpoint
- Docker containerization

**Phase 4: Advanced Capabilities**
- Historical error database
- Pattern learning from repeated diagnostics
- Custom agent addition via plugin system
- Integration with monitoring tools

## Development Context

Built to demonstrate:
- Production-grade multi-agent LLM systems
- Clean architecture principles in Python
- Practical applications of prompt engineering
- DataOps automation patterns

Portfolio project showcasing senior-level skills in LLM integration, API design, and data engineering workflows.

## License

MIT