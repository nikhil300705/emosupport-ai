from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

# ✅ NO VALIDATION AT ALL
@app.post("/reset")
async def reset(request: Request):
    try:
        await request.json()   # accept if exists
    except:
        pass
    return {"status": "ok"}

# ✅ SAME HERE
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