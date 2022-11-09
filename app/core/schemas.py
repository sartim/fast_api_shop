import datetime

from pydantic import BaseModel
from pydantic import Field


class BaseSchema(BaseModel):
    id: int = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()

    class Config:
        json_encoders = {datetime: lambda dt: int(dt.timestamp())}
