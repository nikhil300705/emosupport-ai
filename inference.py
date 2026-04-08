from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}


# ✅ MUST ACCEPT JSON BODY (even if unused)
@app.post("/reset")
async def reset(request: Request):
    data = await request.json()  # <-- THIS IS THE KEY
    return {"status": "ok"}


# ✅ MUST ACCEPT JSON BODY
@app.post("/step")
async def step(request: Request):
    data = await request.json()

    return {
        "observation": "ok",
        "reward": 0.5,
        "done": False,
        "info": {}
    }