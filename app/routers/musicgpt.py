from fastapi import APIRouter
from pydantic import BaseModel
from app.services.musicgpt_service import (
    generate_cover_song,
    generate_music_from_prompt,
    get_task_status
)

router = APIRouter(prefix="/musicgpt", tags=["musicgpt"])


class CoverSongPayload(BaseModel):
    audio_url: str
    voice_id: str
    pitch: int = 0
    webhook_url: str | None = None


@router.post("/cover-song")
def create_cover_song(payload: CoverSongPayload):
    return generate_cover_song(
        audio_url=payload.audio_url,
        voice_id=payload.voice_id,
        pitch=payload.pitch,
        webhook_url=payload.webhook_url
    )


class MusicPromptPayload(BaseModel):
    prompt: str


@router.post("/generate-music")
def generate_music(payload: MusicPromptPayload):
    return generate_music_from_prompt(payload.prompt)


@router.get("/status/{task_id}")
def get_status(task_id: str):
    return get_task_status(task_id)
