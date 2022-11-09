from typing import Union
from app import app


@app.get("/user")
async def list_user():
    return {"results": {}}


@app.get("/user/{user_id}")
async def get_user(user_id: int, q: Union[str, None] = None):
    return {"user_id": user_id, "q": q}


@app.put("/user/{user_id}")
async def update_user(user_id: int, q: Union[str, None] = None):
    return {"user_id": user_id, "q": q}


@app.put("/user/{user_id}")
async def delete_user(user_id: int, q: Union[str, None] = None):
    return {"user_id": user_id, "q": q}
