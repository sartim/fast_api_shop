import datetime

from pydantic import Field


class BaseSchema:
    id: int = Field(example="26")
    created_at: datetime = Field()
    updated_at: datetime = Field()

    class Config:
        json_encoders = {datetime: lambda dt: int(dt.timestamp())}
