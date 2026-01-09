"""
Electronics Product RAG - FastAPI Application

This is the main entry point for the backend API.
It provides endpoints for chatting with the product assistant agent.

Endpoints:
- GET  /health          - Health check
- POST /api/chat        - Chat with the agent (non-streaming)
- POST /api/chat/stream - Chat with the agent (streaming SSE)
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from app.agent import router as agent_router

# Load environment variables
load_dotenv(override=True)

# Create FastAPI app
app = FastAPI(
    title="Electronics Product RAG",
    description="A RAG-based product recommendation agent for electronics",
    version="1.0.0",
)

# Configure CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check():
    """
    Health check endpoint.

    Returns basic status information about the API.
    """
    return {
        "status": "healthy",
        "service": "electronics-product-rag",
        "version": "1.0.0",
    }


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": "Electronics Product RAG API",
        "docs": "/docs",
        "endpoints": {
            "chat": "POST /api/chat",
            "chat_stream": "POST /api/chat/stream",
            "health": "GET /health",
        },
    }


# Include the agent router
app.include_router(agent_router, prefix="/api")
