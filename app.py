from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/reset")
async def reset(request: Request):
    # DO NOT enforce body
    try:
        await request.body()  # just read if exists
    except:
        pass

    return {"status": "ok"}