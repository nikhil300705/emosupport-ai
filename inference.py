from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ResetRequest(BaseModel):
    task: str

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/reset")
def reset(req: ResetRequest):
    return {"status": "ok"}

@app.post("/step")
def step():
    return {
        "observation": "ok",
        "reward": 0.5,
        "done": False,
        "info": {}
    }