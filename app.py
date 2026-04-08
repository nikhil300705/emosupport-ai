from fastapi import FastAPI, Body

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

# ✅ THIS IS THE KEY FIX
@app.post("/reset")
async def reset(body: dict = Body(...)):
    return {"status": "ok"}

@app.post("/step")
async def step(body: dict = Body(...)):
    return {
        "observation": "ok",
        "reward": 0.5,
        "done": False,
        "info": {}
    }