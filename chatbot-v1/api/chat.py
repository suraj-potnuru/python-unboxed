#pylint: disable=C0304
"""
Seperate chat POST endpoint
"""
import os
from google import genai
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from lib import SessionManager, PromptTemplates

GEMINI_MODEL_ID = os.environ.get("GEMINI_MODEL_ID", "gemini-2.5-flash")

router = APIRouter()
client = genai.Client()

@router.post("/api/chat")
async def chat_function(request: Request):
    """
    Chat POST endpoint to accept input messages and return responses from LLM
    """
    try:
        payload = await request.json()
        message = payload.get("message", "")
        session_id = payload.get("session_id", None)
        print(session_id)
        print(message)
        session_manager = SessionManager()

        if session_id is not None:
            print("Loading session from the session id passed")
            session_manager.load_session(session_id)
        else:
            session_id = session_manager.create_session()

        session_manager.session_context.append({"role": "user", "content": message})
        response = client.models.generate_content(
            model=GEMINI_MODEL_ID,
            contents=PromptTemplates.chat_prompt(session_manager.session_context)
        )
        response_message = response.text
        session_manager.session_context.append(
            {"role": "assistant", "content": response_message}
        )

        session_manager.save_session()

        return JSONResponse(status_code=200, content = {
            "message": response_message, "session_id": session_manager.session_id
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e