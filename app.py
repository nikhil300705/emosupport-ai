from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

# ✅ NO validation, no schema
@app.post("/reset")
async def reset(request: Request):
    try:
        await request.body()   # just consume raw body (no JSON parsing)
    except:
        pass
    return {"status": "ok"}

# ✅ same here
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