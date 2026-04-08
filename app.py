from fastapi import FastAPI, Body
from typing import Optional, Dict

app = FastAPI()

@app.post("/reset")
async def reset(body: Optional[Dict] = Body(default=None)):
    return {"status": "ok"}

@app.post("/step")
async def step(body: Optional[Dict] = Body(default=None)):
    return {
        "observation": "ok",
        "reward": 0.5,
        "done": False,
        "info": {}
    }