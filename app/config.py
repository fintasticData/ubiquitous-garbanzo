import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    SUPABASE_URL: str = os.getenv("SUPABASE_URL")
    SUPABASE_KEY: str = os.getenv("SUPABASE_SERVICE_KEY")
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")
    MUSICGPT_API_KEY: str = os.getenv("MUSICGPT_API_KEY")
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"

settings = Settings()
