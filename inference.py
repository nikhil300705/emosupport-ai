from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

# 🔥 FORCE ACCEPT ANY REQUEST (WITH OR WITHOUT BODY)
@app.post("/reset")
async def reset(request: Request):
    try:
        await request.json()  # try reading body if exists
    except:
        pass  # ignore if no body

    return {"status": "ok"}


@app.post("/step")
async def step(request: Request):
    try:
        await request.json()
    except:
        pass

    return {
        "observation": "ok",
        "reward": 0.5,
        "done": False,
        "info": {}
    }