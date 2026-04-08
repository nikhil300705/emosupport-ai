from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
def root():
    return {"status": "running"}


@app.post("/reset")
async def reset():
    return JSONResponse(content={"status": "ok"})


@app.post("/step")
async def step():
    return JSONResponse(content={
        "observation": "ok",
        "reward": 0.5,
        "done": False,
        "info": {}
    })