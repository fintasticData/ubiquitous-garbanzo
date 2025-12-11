from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import health, dynamic, ai_tools, musicgpt

origins = [
    "*",  # better to restrict later
]

app = FastAPI(title="uG — Ubiquitous Garbanzo Engine")

# --- CORS Middleware ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Routers ---
app.include_router(health.router)
app.include_router(dynamic.router)
app.include_router(ai_tools.router)
app.include_router(musicgpt.router)

@app.get("/")
def root():
    return {"status": "uG engine running", "version": "0.1"}
