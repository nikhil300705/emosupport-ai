from fastapi import FastAPI
from fastapi.routing import APIRoute

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}


@app.post("/reset", openapi_extra={"requestBody": None})
def reset():
    return {"status": "ok"}


@app.post("/step", openapi_extra={"requestBody": None})
def step():
    return {
        "observation": "ok",
        "reward": 0.5,
        "done": False,
        "info": {}
    }


# 🔥 FORCE REMOVE REQUEST BODY FROM OPENAPI
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = app.openapi()

    for path in openapi_schema["paths"].values():
        for method in path.values():
            method.pop("requestBody", None)

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi