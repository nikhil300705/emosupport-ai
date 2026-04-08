from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class ResetRequest(BaseModel):
    task: Optional[str] = "default"

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/reset")
def reset(req: Optional[ResetRequest] = None):
    return {"status": "ok"}

@app.post("/step")
def step():
    return {
        "observation": "ok",
        "reward": 0.5,
        "done": False,
        "info": {}
    }