# AI PRD Generator

A production-ready FastAPI backend that generates structured Product Requirement Documents (PRDs) from a single product idea using LLMs (Ollama / OpenAI / Anthropic Claude).

## Architecture

```
Client → FastAPI Router → Module Router → Service → Orchestrator → Infra (LLM) → Provider → Response
```

Feature-based modular structure with clean separation of concerns:

- **`app/core/`** – Config, logging, exceptions, dependency injection
- **`app/modules/`** – Feature modules (health, prd)
- **`app/infra/`** – External service abstractions (LLM, DB, cache)
- **`app/shared/`** – Utilities and constants

## Quick Start

### 1. Install dependencies

```bash
make install
```

Or manually:

```bash
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure environment

Copy `.env.example` to `.env` and configure:

```
LLM_PROVIDER=ollama
LLM_BASE_URL=https://your-ngrok-url.ngrok-free.dev/api/generate
MODEL_NAME=llama3

# For OpenAI / Anthropic (swap LLM_PROVIDER accordingly):
# LLM_API_KEY=sk-...
# LLM_PROVIDER=openai
# LLM_BASE_URL=https://api.openai.com/v1
# MODEL_NAME=gpt-4o-mini
```

### 3. Run the server

```bash
make dev     # with hot-reload
make run     # without hot-reload
```

Or manually:

```bash
uvicorn app.main:app --reload
```

### 4. Try it out

- Health check: [http://localhost:8000/health](http://localhost:8000/health)
- Swagger docs: [http://localhost:8000/docs](http://localhost:8000/docs)

Generate a PRD:

```bash
curl -X POST http://localhost:8000/generate-prd \
  -H "Content-Type: application/json" \
  -d '{"idea": "Build an AI meeting assistant"}'
```

## APIs

| Method | Endpoint         | Description                |
|--------|------------------|----------------------------|
| GET    | `/health`        | Health check               |
| POST   | `/generate-prd`  | Generate a full PRD        |

## Project Structure

```
ai-prd-generator/
├── app/
│   ├── main.py
│   ├── api_router.py
│   ├── core/
│   │   ├── config.py
│   │   ├── logger.py
│   │   ├── exceptions.py
│   │   └── dependencies.py
│   ├── modules/
│   │   ├── health/
│   │   │   ├── router.py
│   │   │   └── service.py
│   │   └── prd/
│   │       ├── router.py
│   │       ├── service.py
│   │       ├── orchestrator.py
│   │       ├── schema.py
│   │       └── prompts.py
│   ├── infra/
│   │   ├── llm/
│   │   │   ├── base.py
│   │   │   ├── ollama_client.py
│   │   │   ├── openai_client.py
│   │   │   └── anthropic_client.py
│   │   ├── db/
│   │   └── cache/
│   └── shared/
│       ├── utils.py
│       └── constants.py
├── tests/
│   ├── unit/
│   └── integration/
├── requirements.txt
├── Makefile
├── .env
├── .env.example
├── .gitignore
└── README.md
```

## Next Steps

- PostgreSQL integration
- Vector DB for RAG
- Analytics module
- Agent workflows
- Frontend
