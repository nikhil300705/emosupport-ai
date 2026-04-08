from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}


# REQUIRED endpoint
@app.post("/reset")
async def reset(request: Request):
    try:
        await request.body()
    except:
        pass
    return {"status": "ok"}


# REQUIRED endpoint
@app.post("/step")
async def step(request: Request):
    try:
        await request.body()
    except:
        pass

    return {
        "observation": "ok",
        "reward": 0.5,
        "done": False,
        "info": {}
    }