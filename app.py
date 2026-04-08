from fastapi import FastAPI, Body
from typing import Optional

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

# ✅ BODY MUST BE OPTIONAL
@app.post("/reset")
async def reset(body: Optional[dict] = Body(default=None)):
    return {"status": "ok"}

# ✅ BODY MUST BE OPTIONAL
@app.post("/step")
async def step(body: Optional[dict] = Body(default=None)):
    return {
        "observation": "ok",
        "reward": 0.5,
        "done": False,
        "info": {}
    }