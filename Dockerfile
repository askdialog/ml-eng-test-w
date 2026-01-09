# Electronics Product RAG - Dockerfile
# Multi-stage build for development and production

# Stage 1: Frontend build
FROM node:20-alpine AS frontend-builder

WORKDIR /app/frontend

# Copy package files
COPY frontend/package.json ./

# Install dependencies
RUN npm install

# Copy source
COPY frontend/ ./

# Build the frontend
RUN npm run build

# Stage 2: Python backend
FROM python:3.12-slim AS production

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv for fast Python package management
RUN pip install uv

WORKDIR /app

# Copy backend requirements and install
COPY backend/pyproject.toml backend/README.md ./backend/

WORKDIR /app/backend

# Install Python dependencies (without installing the project itself)
RUN uv sync --no-dev --no-install-project

# Copy backend source
COPY backend/ ./

# Copy data and evaluation
COPY data/ /app/data/
COPY evaluation/ /app/evaluation/

# Copy frontend build (static files for serving)
COPY --from=frontend-builder /app/frontend/.next /app/frontend/.next
COPY --from=frontend-builder /app/frontend/public /app/frontend/public
COPY --from=frontend-builder /app/frontend/node_modules /app/frontend/node_modules
COPY --from=frontend-builder /app/frontend/package.json /app/frontend/

# Set environment variables
ENV PYTHONPATH=/app/backend:/app
ENV PYTHONUNBUFFERED=1

# Expose ports
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Default command - run backend
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
