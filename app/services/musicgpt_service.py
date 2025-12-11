import requests
from app.config import settings


BASE_URL = "https://api.musicgpt.com/api/public/v1"


def generate_cover_song(audio_url: str, voice_id: str, pitch: int = 0, webhook_url: str | None = None):
    url = f"{BASE_URL}/Cover"

    headers = {
        "Authorization": settings.MUSICGPT_API_KEY
    }

    payload = {
        "audio_url": audio_url,
        "voice_id": voice_id,
        "pitch": pitch,
    }

    if webhook_url:
        payload["webhook_url"] = webhook_url

    response = requests.post(url, headers=headers, data=payload)
    return response.json()


def generate_music_from_prompt(prompt: str):
    url = f"{BASE_URL}/Music"

    headers = {
        "Authorization": settings.MUSICGPT_API_KEY,
        "Content-Type": "application/json",
    }

    payload = {"prompt": prompt}

    response = requests.post(url, headers=headers, json=payload)
    return response.json()


def get_task_status(task_id: str):
    url = f"{BASE_URL}/Status/{task_id}"

    headers = {"Authorization": settings.MUSICGPT_API_KEY}

    response = requests.get(url, headers=headers)
    return response.json()
