from fastapi import FastAPI
from app.core.session import create_session

app = FastAPI(
    title="Shop API",
    description="Shop API",
    version="0.0.1",
)
db = create_session()


@app.get("/")
async def read_root():
    return {"status": "Ok"}
