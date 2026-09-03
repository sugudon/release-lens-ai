# ReleaseLens AI

## AI-Powered Software Release Risk & Change-Impact Copilot

ReleaseLens AI is a RAG-based AI assistant for software engineering teams. It analyzes a proposed software release against engineering knowledge such as architecture documentation, ADRs, incident reports, runbooks, testing guidelines, and previous release information.

The goal is to identify potentially affected components, historical risks, relevant engineering decisions, and recommended testing based on retrieved evidence.

## Problem

Software release information is often distributed across multiple engineering documents. Before releasing a change, engineers need to determine:

- What components may be affected?
- Have similar changes caused incidents before?
- Which architecture decisions are relevant?
- What tests should be executed?
- What risks should be considered?
- Is there enough evidence to make a reliable recommendation?

ReleaseLens AI brings this information together through semantic retrieval and LLM-based analysis.

## Solution

```text
Release Description
        ↓
Query Processing
        ↓
Document Retrieval
        ↓
Relevant Engineering Evidence
        ↓
LLM Analysis
        ↓
Release Impact & Risk Report
```

The system grounds its responses in retrieved engineering documents and identifies when available evidence is insufficient.

## Core Features

- Release change analysis
- Impacted component identification
- Risk assessment
- Historical incident discovery
- Architecture and ADR analysis
- Testing recommendations
- Evidence-backed responses
- Source citations
- Uncertainty / abstention handling
- Semantic document retrieval
- LangSmith tracing and evaluation

## RAG Pipeline

```text
Engineering Documents
        ↓
Data Ingestion
        ↓
Text Splitting
        ↓
Embeddings
        ↓
Vector Store
        ↓
Retriever
        ↓
Relevant Context
        ↓
Prompt
        ↓
LLM
        ↓
Structured Release Analysis
```

## Knowledge Base

The project uses a structured engineering knowledge base containing:

```text
knowledge_base/
├── architecture/
├── adr/
├── incidents/
├── runbooks/
├── testing/
└── releases/
```

Example knowledge:

- Frontend and backend architecture
- Service dependencies
- Architecture decisions
- Previous production incidents
- Deployment and operational runbooks
- Testing requirements
- Previous release changes

## LangChain

LangChain is used to implement the complete RAG workflow:

- Document loaders
- Text splitters
- Embeddings
- Vector stores
- Retrievers
- Prompt templates
- Chat models
- Output parsers
- LCEL chains

Example chain:

```python
chain = prompt | model | StrOutputParser()
```

The final RAG chain combines retrieval, prompt construction, LLM generation, and output parsing.

## LangSmith

LangSmith provides observability and evaluation for the ReleaseLens AI pipeline.

It is used to monitor:

- RAG traces
- Retriever behavior
- Retrieved context
- Prompt execution
- LLM responses
- Latency
- Token usage
- Errors
- Evaluation results
- User feedback

## Evaluation

ReleaseLens AI evaluates both retrieval and generation quality.

Evaluation areas include:

- Context relevance
- Retrieval quality
- Answer correctness
- Faithfulness to retrieved evidence
- Citation correctness
- Impact detection
- Risk classification
- Testing recommendations
- Appropriate abstention when evidence is insufficient

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

## Example

### Release Request

```text
Migrate Payment API v1 to Payment API v2
and change the payment retry mechanism.
```

### Analysis

```text
Risk Level: High

Potentially affected:
- Payment Service
- Checkout
- Retry Handling

Relevant evidence:
- Payment API architecture
- Payment API migration ADR
- Previous payment timeout incident
- Payment testing guidelines

Recommended testing:
- API contract testing
- Integration testing
- Checkout regression testing
- Failure scenario testing
- Load testing
```

## Key Design Principle

ReleaseLens AI follows an evidence-first approach:

```text
Relevant Evidence
       ↓
Reasoning
       ↓
Recommendation
```

If sufficient evidence cannot be retrieved, the system should communicate the uncertainty instead of generating unsupported claims.

## Project Goal

The project demonstrates how LangChain, RAG, LLMs, and LangSmith can be combined to build an AI system for a realistic software engineering use case rather than a basic document-question-answering chatbot.
