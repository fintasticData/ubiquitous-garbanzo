from fastapi import APIRouter
from pydantic import BaseModel
from app.utils.script_runner import run_script_dynamic

router = APIRouter(prefix="/dynamic", tags=["dynamic"])

class ScriptPayload(BaseModel):
    script: str
    context: dict | None = None

@router.post("/run_script")
async def run_script(payload: ScriptPayload):
    return run_script_dynamic(payload.script, payload.context)
