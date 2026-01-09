# AI Engineer Take-Home Assignment: Electronics Product RAG

## Overview

Build a **Retrieval-Augmented Generation (RAG)** system for an electronics product catalog. Your system should help customers find products through natural language queries and provide relevant recommendations.


You can (and you probably should) use any AI tooling at your disposal!

You can take shortcuts, as long as you can explain in the debrief why you took them and what would be the most appropriate implementation if you had more time.

## Quick Start

### Prerequisites

- Docker

### Running the Application

```bash
# Copy environment file and add your API keys if needed
cp .env.example .env

# Start the application
docker-compose up
```

Access:

- Backend API: http://localhost:8000
- Frontend UI: http://localhost:3000

## Assignment Parts

### Part A: RAG Implementation

1. Data Ingestion & Indexing

- Design and implement a strategy to index product data for efficient retrieval
- Consider what information should be indexed and how

2. Retrieval

Implement a retrieval system that can search through the product catalog (`data/products.json`) and return relevant results for user queries.

- Implement semantic search to find relevant products given a user query
- You may use any embedding model and vector store (local is fine)


See `backend/app/agent.py` for example code. Streaming support is optional, but an example is provided if needed.

3. Orchestration

Implement the answer generation. You may use any existing/popular library or provide all the code yourself.

### Part B: Evaluation

Build a simple evaluation framework to measure the quality of your retrieval system using the sample queries provided in `data/sample_queries.json`.

### Part C: Documentation

Document your design decisions, trade-offs, and evaluation results.

## Submission

1. Complete your implementation
2. Push to a private GitHub repository
3. Share access with the Dialog team

---

Good luck! We're excited to see your solution.
