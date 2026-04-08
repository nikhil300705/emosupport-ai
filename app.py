from fastapi import FastAPI, Body
from typing import Optional, Dict

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

# ✅ ACCEPTS both: with body OR without body
@app.post("/reset")
async def reset(body: Optional[Dict] = Body(default=None)):
    return {"status": "ok"}

# ✅ SAME FIX HERE
@app.post("/step")
async def step(body: Optional[Dict] = Body(default=None)):
    return {
        "observation": "ok",
        "reward": 0.5,
        "done": False,
        "info": {}
    }