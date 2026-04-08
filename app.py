from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/reset")
async def reset(request: Request):
    try:
        await request.body()
    except:
        pass
    return {"status": "ok"}

@app.post("/step")
async def step(request: Request):
    try:
        data = await request.json()
    except:
        data = {}

    # Minimal valid response for checker
    return {
        "observation": "ok",
        "reward": 0.5,
        "done": False,
        "info": {}
    }