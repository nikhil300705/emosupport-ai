from fastapi import FastAPI, Body

app = FastAPI()

@app.post("/reset")
async def reset(body: dict = Body(...)):
    return {"status": "ok"}

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