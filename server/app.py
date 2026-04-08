from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ResetRequest(BaseModel):
    task: str = "default"

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/reset")
def reset(req: ResetRequest):
    return {
        "observation": f"Reset done for task: {req.task}",
        "reward": 0.0,
        "done": False,
        "info": {}
    }

@app.post("/step")
def step(action: dict):
    return {
        "observation": "step executed",
        "reward": 0.1,
        "done": False,
        "info": {}
    }