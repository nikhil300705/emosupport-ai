from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
def root():
    return {"status": "running"}


@app.post("/reset")
async def reset(request: Request):
    body = await request.json()  # accept any body (important)
    return {"status": "ok"}