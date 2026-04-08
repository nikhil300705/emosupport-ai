from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

# ✅ MUST accept request body
@app.post("/reset")
async def reset(request: Request):
    await request.json()  # consume body
    return {"status": "ok"}

# ✅ MUST accept request body
@app.post("/step")
async def step(request: Request):
    await request.json()  # consume body
    return {
        "observation": "ok",
        "reward": 0.5,
        "done": False,
        "info": {}
    }