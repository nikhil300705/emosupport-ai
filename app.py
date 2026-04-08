from fastapi import FastAPI, Body

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

# ✅ REQUIRED BODY BUT ACCEPT EMPTY {}
@app.post("/reset")
async def reset(body: dict = Body(default={})):
    return {"status": "ok"}

# ✅ SAME HERE
@app.post("/step")
async def step(body: dict = Body(default={})):
    return {
        "observation": "ok",
        "reward": 0.5,
        "done": False,
        "info": {}
    }