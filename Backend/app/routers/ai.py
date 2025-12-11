from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.ai.switcher import run_ai_model

router = APIRouter()


# ----------- Request Schema -----------
class AIRequest(BaseModel):
    prompt: str
    model: str | None = None


# ----------- Endpoints -----------
@router.post("/generate")
async def generate_ai_text(data: AIRequest):
    if not data.prompt:
        raise HTTPException(status_code=400, detail="Prompt cannot be empty")

    response = await run_ai_model(data.prompt, data.model)
    return {"response": response}
