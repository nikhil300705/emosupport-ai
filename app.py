from fastapi import FastAPI, Body
from typing import Any

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/reset")
def reset(body: Any = Body(default={})):
    return {"status": "ok"}