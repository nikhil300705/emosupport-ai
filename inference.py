from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

# ✅ NO BODY PARAMETER AT ALL
@app.post("/reset")
def reset():
    return {"status": "ok"}

# ✅ NO BODY PARAMETER AT ALL
@app.post("/step")
def step():
    return {
        "observation": "ok",
        "reward": 0.5,
        "done": False,
        "info": {}
    }