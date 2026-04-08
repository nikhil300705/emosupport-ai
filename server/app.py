from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
def root():
    return {"status": "running"}


@app.post("/reset")
async def reset(request: Request):
    try:
        await request.json()  # try reading body
    except:
        pass  # ignore if empty

    return {"status": "ok"}