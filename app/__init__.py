from fastapi import FastAPI

app = FastAPI(
    title="test",
    description="test",
    version="0.0.1",
)


@app.get("/")
async def read_root():
    return {"status": "Ok"}
