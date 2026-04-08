from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"status": "running"}


@app.post("/reset")
def reset():
    return {"status": "ok"}