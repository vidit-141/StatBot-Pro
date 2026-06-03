<div align="center">

# StatBot Pro

### *Your Data Has a Story. Let AI Tell It.*

[![Next.js](https://img.shields.io/badge/Next.js-14-black?style=for-the-badge&logo=next.js)](https://nextjs.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![LangChain](https://img.shields.io/badge/LangChain-Agent-1C3C3C?style=for-the-badge&logo=chainlink)](https://langchain.com)
[![GPT-4o](https://img.shields.io/badge/GPT--4o-Powered-412991?style=for-the-badge&logo=openai)](https://openai.com)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)](https://python.org)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker)](https://docker.com)

> Upload any CSV or Excel file, ask a question in plain English, and get instant answers and charts — powered by a self-correcting LangChain agent with a sandboxed Python execution engine.

</div>

---

## Overview

StatBot Pro is an autonomous data analyst agent built for business users who need insights from spreadsheet data without writing code. The user uploads a file and asks a question — the AI writes the pandas code, executes it safely, self-corrects on errors, and returns the answer along with any generated charts.

---

## Architecture

# StatBot-Pro Architecture

```text
statbot-pro/
│
├── backend/                           # FastAPI + LangGraph backend
│   │
│   ├── main.py                        # Application entrypoint, CORS, static serving
│   │
│   └── app/
│       │
│       ├── routers/                   # API endpoints
│       │   ├── analysis.py            # POST /api/analysis/upload-and-ask
│       │   └── health.py              # GET /api/health
│       │
│       ├── services/                  # Core business logic
│       │   ├── agent.py               # LangGraph ReAct agent + self-correction
│       │   ├── file_handler.py        # CSV/Excel parsing & validation
│       │   └── session_store.py       # In-memory conversation history
│       │
│       ├── models/                    # Data schemas
│       │   └── schemas.py             # Pydantic request/response models
│       │
│       └── utils/
│           └── sandbox.py             # Restricted Python execution engine
│
├── frontend/                          # Next.js 14 App Router
│   │
│   └── src/
│       │
│       ├── app/                       # Pages and global styles
│       ├── components/                # UI components
│       │   ├── FileDropzone
│       │   ├── AgentThinking
│       │   └── AnalysisResult
│       │
│       ├── lib/                       # Axios API client + config
│       └── types/                     # Shared TypeScript types
│
├── docker-compose.yml                 # One-command full stack startup
│
└── README.md                          # Project documentation
```


## Quick Start

### Option A — Docker Compose

```bash
git clone https://github.com/your-org/statbot-pro.git
cd statbot-pro
cp backend/.env.example backend/.env
# Add your OPENAI_API_KEY to backend/.env
docker-compose up --build
```

App: http://localhost:3000 — API Docs: http://localhost:8000/docs

---

### Option B — Local Development

**Backend**
```bash
cd backend
python -m venv venv
venv\Scripts\Activate.ps1        # Windows
pip install -r requirements.txt
cp .env.example .env             # add OPENAI_API_KEY
python -m uvicorn main:app --reload --port 8000
```

**Frontend**
```bash
cd frontend
npm install
cp .env.local.example .env.local
npm run dev
```

---

## Environment Variables

**backend/.env**

| Variable | Default | Required | Description |
|---|---|---|---|
| `OPENAI_API_KEY` | — | Yes | OpenAI secret key |
| `OPENAI_MODEL` | `gpt-4o` | No | Model used by the agent |
| `MAX_ITERATIONS` | `10` | No | Max self-correction retries |
| `CHARTS_DIR` | `static/charts` | No | Directory for saved chart PNGs |
| `CHARTS_BASE_URL` | `http://localhost:8000/static/charts` | No | Public URL for chart serving |
| `ALLOWED_ORIGINS` | `http://localhost:3000` | No | CORS allowed origins |

**frontend/.env.local**

| Variable | Default | Description |
|---|---|---|
| `NEXT_PUBLIC_API_URL` | `http://localhost:8000` | Backend base URL |

---

## API Reference

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/health` | Health check |
| `POST` | `/api/analysis/preview` | Upload file, returns column info and sample data |
| `POST` | `/api/analysis/upload-and-ask` | Upload file + question, returns answer and charts |
| `GET` | `/api/analysis/session/{id}/history` | Get conversation history for a session |
| `DELETE` | `/api/analysis/session/{id}` | Clear session history |

---

## Security

All AI-generated code runs inside a sandboxed REPL before being executed. A static pattern scanner blocks dangerous operations before execution even begins.

**Blocked:** `os`, `subprocess`, `shutil`, `socket`, `requests`, `urllib`, `open()`, `eval()`, `exec()`, `__import__()`

**Allowed:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `datetime`, `math`, `re`, `json`

---

## Feature Status

| Feature | Status |
|---|---|
| FastAPI backend with CORS and static file serving | Done |
| CSV / Excel upload, parsing, dtype inference | Done |
| Dataset preview endpoint | Done |
| LangGraph ReAct agent with self-correction | Done |
| Sandboxed Python REPL with static pattern check | Done |
| Chart generation via matplotlib/seaborn | Done |
| Rate limiting — 10 requests/minute per IP | Done |
| Session memory for follow-up questions | Done |
| Next.js 14 frontend with drag-and-drop upload | Done |
| Animated agent thinking indicator | Done |
| Docker Compose full stack setup | Done |
| WebSocket streaming of agent thought process | Planned |
| Redis session persistence | Planned |
| PDF report export | Planned |

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Next.js 14, TypeScript, Tailwind CSS |
| Backend | FastAPI, Python 3.11 |
| AI Agent | LangChain, LangGraph, GPT-4o |
| Data Processing | Pandas, NumPy |
| Visualisation | Matplotlib, Seaborn |
| Infrastructure | Docker, Docker Compose |

---

<div align="center">
Built as an internship project at Infotact Solutions
</div>