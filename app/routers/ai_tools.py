from fastapi import APIRouter
from app.services.gemini_service import generate_text

router = APIRouter(prefix="/ai", tags=["ai"])

@router.post("/gemini")
async def gemini_generate(prompt: str):
    return generate_text(prompt)
