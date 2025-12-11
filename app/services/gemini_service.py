import requests
from app.config import settings

def generate_text(prompt: str):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateText?key={settings.GEMINI_API_KEY}"
    payload = {"prompt": {"text": prompt}}
    res = requests.post(url, json=payload)
    return res.json()
