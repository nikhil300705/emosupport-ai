from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

# ✅ MUST READ BODY (important)
@app.post("/reset")
async def reset(request: Request):
    try:
        await request.json()  # 👈 this line fixes the error
    except:
        pass
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