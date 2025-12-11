from fastapi import FastAPI
from app.routers import health, dynamic, ai_tools

app = FastAPI(title="uG — Ubiquitous Garbanzo Engine")

app.include_router(health.router)
app.include_router(dynamic.router)
app.include_router(ai_tools.router)

@app.get("/")
def root():
    return {"status": "uG engine running", "version": "0.1"}
