from fastapi import FastAPI
from v1.api import router as api_router

app = FastAPI()

app.include_router(api_router, prefix="/v1", tags=["v1"])


@app.get("/")
def read_root():
    return {"message": "Hello World!"}
