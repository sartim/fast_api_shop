import datetime

from pydantic import Field

from app.core.schemas import BaseSchema


class UserSchema(BaseSchema):
    id: str = Field()
    first_name: str = Field()
    middle_name: str = Field()
    last_name: str = Field()
