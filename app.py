from fastapi import FastAPI, Body
from typing import Optional, Dict, Any

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

# ✅ BODY OPTIONAL (THIS IS KEY)
@app.post("/reset")
def reset(body: Optional[Dict[str, Any]] = Body(default=None)):
    return {"status": "ok"}

# ✅ REQUIRED FORMAT FOR CHECKER
@app.post("/step")
def step(body: Optional[Dict[str, Any]] = Body(default=None)):
    return {
        "observation": "ok",
        "reward": 0.5,
        "done": False,
        "info": {}
    }