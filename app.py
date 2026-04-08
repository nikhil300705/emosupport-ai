from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Optional body model
class ResetRequest(BaseModel):
    task: Optional[str] = "default"

@app.get("/")
def root():
    return {"status": "running"}

# ✅ RESET (works with OR without body)
@app.post("/reset")
def reset(req: Optional[ResetRequest] = None):
    return {"status": "ok"}

# ✅ STEP (no body required)
@app.post("/step")
def step():
    return {
        "observation": "ok",
        "reward": 0.5,
        "done": False,
        "info": {}
    }