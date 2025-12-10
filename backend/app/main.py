from fastapi import FastAPI
from backend.app.api.endpoints import chat
from fastapi_limiter import FastAPILimiter
import redis.asyncio as redis
import os

app = FastAPI()

@app.on_event("startup")
async def startup():
    REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379")
    redis_instance = redis.from_url(REDIS_URL, encoding="utf-8", decode_responses=True)
    await FastAPILimiter.init(redis_instance)

app.include_router(chat.router, prefix="/api")

@app.get("/")
def read_root():
    return {"Hello": "RAG Chatbot Backend"}
