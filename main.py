import asyncio
import uvicorn

from app import app
from app.user import api


async def create_app(scope, receive, send):
    return app


async def main():
    config = uvicorn.Config("main:app", port=5000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())
