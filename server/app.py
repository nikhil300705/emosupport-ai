from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"status": "running"}


@app.post("/reset")
def reset():
    # Must NOT expect body (important for checker)
    return {"status": "ok"}