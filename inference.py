from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "inference running"}

def main():
    return app
