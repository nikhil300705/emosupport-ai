from fastapi import FastAPI, Body
from typing import Any

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

# ✅ Accept ANY body, optional, no validation issues
@app.post("/reset")
async def reset(body: Any = Body(default=None)):
    return {"status": "ok"}

# ✅ Same for step
@app.post("/step")
async def step(body: Any = Body(default=None)):
    return {
        "observation": "ok",
        "reward": 0.5,
        "done": False,
        "info": {}
    }