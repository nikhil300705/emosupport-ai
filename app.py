from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# ✅ Request body model (IMPORTANT)
class ResetRequest(BaseModel):
    task: str

@app.get("/")
def root():
    return {"status": "running"}

# ✅ FIXED: now accepts body
@app.post("/reset")
def reset(req: ResetRequest):
    return {"status": "ok"}

# ✅ step endpoint
@app.post("/step")
def step():
    return {
        "observation": "ok",
        "reward": 0.5,
        "done": False,
        "info": {}
    }