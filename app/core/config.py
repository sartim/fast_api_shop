import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url = os.environ.get("DATABASE_URL")
