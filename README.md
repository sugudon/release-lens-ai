# ReleaseLens AI

AI-Powered Software Release Risk & Change-Impact Copilot.

ReleaseLens AI is a production-oriented RAG application designed to analyze proposed software releases against engineering knowledge such as architecture documentation, ADRs, incident reports, runbooks, testing guidelines, and previous releases.

The system follows an evidence-first approach:

Relevant Evidence
        ↓
Reasoning
        ↓
Recommendation

If sufficient evidence cannot be retrieved, the system communicates uncertainty instead of inventing information.

## Technology Stack

### AI
- Python
- LangChain
- OpenAI
- LangSmith

### RAG
- Document Loaders
- Text Splitters
- Embeddings
- Vector Search
- Retrievers
- Reranking
- Metadata Filtering

### Backend
- FastAPI
- PostgreSQL
- pgvector

### Frontend
- React
- TypeScript
- Tailwind CSS

### DevOps
- Docker
- GitHub Actions

## Project Structure

```text
release-lens-ai/
├── backend/
├── frontend/
├── knowledge_base/
├── evaluation/
├── scripts/
├── tests/
├── .env.example
├── .gitignore
├── requirements.txt
├── docker-compose.yml
└── README.md