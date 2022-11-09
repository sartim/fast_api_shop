import os


class Config:
    REDIS_URL = os.environ.get("REDIS_URL")
