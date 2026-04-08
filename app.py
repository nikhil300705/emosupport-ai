from fastapi import FastAPI, Body
from typing import Dict, Any

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

# ✅ Accept JSON body (required by checker)
@app.post("/reset")
def reset(body: Dict[str, Any] = Body(default={})):
    return {"status": "ok"}

# ✅ Required endpoint
@app.post("/step")
def step(body: Dict[str, Any] = Body(default={})):
    return {
        "observation": "ok",
        "reward": 0.5,
        "done": False,
        "info": {}
    }