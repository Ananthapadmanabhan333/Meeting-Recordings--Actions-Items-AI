# LuminaOS: Enterprise AI Meeting Intelligence Platform

Welcome to the LuminaOS project repository! LuminaOS is a production-ready, AI-native meeting intelligence operating system.

## 📚 Documentation
Please read the comprehensive architectural blueprint covering System Design, Real-Time Pipelines, AI Agent Orchestration, and deployment configurations:

👉 **[ARCHITECTURE_BLUEPRINT.md](./ARCHITECTURE_BLUEPRINT.md)**

## 🚀 Quick Start (Development)

The project leverages a microservices architecture.

### 1. Infrastructure Services
Start Postgres, Redis, Kafka, and Qdrant:
```bash
docker-compose up -d db redis kafka qdrant
```

### 2. Backend (FastAPI + LangGraph)
```bash
cd backend
python -m venv venv
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
cp ../.env.example .env
uvicorn app.main:app --reload
```

### 3. Frontend (Next.js 15)
```bash
cd frontend
npm install
npm run dev
```

## 🏗️ Stack
- **AI Core**: LangGraph, OpenAI/Anthropic, Pyannote.audio, Faster-Whisper
- **Backend**: FastAPI, Celery, SQLAlchemy, Asyncpg
- **Streaming**: WebRTC, WebSockets, Apache Kafka
- **Database**: PostgreSQL (Relational), Qdrant (Vector)
- **Frontend**: Next.js 15, Tailwind CSS, Framer Motion
