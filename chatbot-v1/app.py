"""
Entry point for the Chatbot API
"""
from api import chat
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI(
    title = "Ollama Chatbot API",
    description="This is a chatbot api powered by Ollama - Gemma3 🚀",
    summary="This API is used to interact with the Ollama Chatbot.",
    version="1.0",
    contact={
        "name": "Suraj Potnuru",
        "url": "https://github.com/suraj-potnuru",
        "email": "surajpotnuru7@gmail.com",
    },
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/v1/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"]
)

app.include_router(chat.router)

@app.get("/api/heartbeat")
async def heartbeat():
    """
    Simple hearbeat endpoint. Returns 200.
    """
    return JSONResponse(status_code=200, content = {"message": "API is running !"})
