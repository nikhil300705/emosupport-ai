from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

# 🔥 NO BODY VALIDATION AT ALL
@app.post("/reset")
async def reset(request: Request):
    return {"status": "ok"}

@app.post("/step")
def step():
    return {
        "observation": "ok",
        "reward": 0.5,
        "done": False,
        "info": {}
    }