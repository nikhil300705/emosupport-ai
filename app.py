from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

# MUST accept empty body AND not validate
@app.post("/reset")
async def reset():
    return {"status": "ok"}

@app.post("/step")
async def step():
    return {
        "observation": "ok",
        "reward": 0.5,
        "done": False,
        "info": {}
    }