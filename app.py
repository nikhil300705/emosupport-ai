from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# ✅ Request body model (REQUIRED for /reset)
class ResetRequest(BaseModel):
    task: str

# ✅ Root check
@app.get("/")
def root():
    return {"status": "running"}

# ✅ RESET (must accept body + return status only)
@app.post("/reset")
def reset(req: ResetRequest):
    return {"status": "ok"}

# ✅ STEP (no body needed)
@app.post("/step")
def step():
    return {
        "observation": "ok",
        "reward": 0.5,
        "done": False,
        "info": {}
    }