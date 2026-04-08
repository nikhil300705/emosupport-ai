from fastapi import FastAPI, Body

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

# ✅ RESET (accepts with OR without body — REQUIRED for Scaler)
@app.post("/reset")
def reset(req: dict = Body(None)):
    return {"status": "ok"}

# ✅ STEP
@app.post("/step")
def step():
    return {
        "observation": "ok",
        "reward": 0.5,
        "done": False,
        "info": {}
    }