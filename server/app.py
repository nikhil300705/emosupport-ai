from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

# IMPORTANT: must accept request WITHOUT body
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

# REQUIRED for openenv validation
def main():
    return app