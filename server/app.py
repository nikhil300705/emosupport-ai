from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/")
def root():
    return {"status": "running"}


@app.post("/reset")
def reset(body: Optional[dict] = None):
    return {"status": "ok"}