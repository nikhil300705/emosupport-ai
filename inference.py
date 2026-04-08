from fastapi import FastAPI

print("INFERENCE RUNNING ✅")

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/reset")
def reset():
    return {"status": "ok"}

@app.post("/step")
def step():
    return {
        "observation": "ok",
        "reward": 0.5,
        "done": False,
        "info": {}
    }