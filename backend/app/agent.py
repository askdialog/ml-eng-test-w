"""
Product Assistant Agent - Simplified stub implementation.
"""

import asyncio
import json
from typing import AsyncGenerator, List
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel


router = APIRouter()


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]


def get_response(user_message: str) -> str:
    return f"You said: '{user_message}'. I'm a stub assistant and can't help yet!"


async def stream_response(message: str) -> AsyncGenerator[str, None]:
    """Stream a message as Server-Sent Events, word by word."""
    words = message.split(' ')
    for i, word in enumerate(words):
        chunk = word if i == 0 else ' ' + word
        yield f"data: {json.dumps({'type': 'text', 'content': chunk})}\n\n"
        await asyncio.sleep(0.03)
    yield f"data: {json.dumps({'type': 'done'})}\n\n"


@router.post("/chat")
async def chat(request: ChatRequest):
    """Chat endpoint - returns a complete response."""
    user_message = request.messages[-1].content if request.messages else ""
    return {"message": get_response(user_message)}


@router.post("/chat/stream")
async def chat_stream(request: ChatRequest) -> StreamingResponse:
    """Streaming chat endpoint - returns Server-Sent Events."""
    user_message = request.messages[-1].content if request.messages else ""
    return StreamingResponse(
        stream_response(get_response(user_message)),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        },
    )
