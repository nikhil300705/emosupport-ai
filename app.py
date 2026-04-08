from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/reset")
async def reset(request=None):
    return {"status": "ok"}

@app.post("/step")
async def step(request=None):
    return {
        "observation": "ok",
        "reward": 0.5,
        "done": False,
        "info": {}
    }