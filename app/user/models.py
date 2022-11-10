import sqlalchemy as sa

from app.core.models import BaseModel
from sqlalchemy.dialects.postgresql import UUID


class User(BaseModel):
    __tablename__ = "user"

    id = sa.Column(UUID(as_uuid=True), primary_key=True)
    first_name = sa.Column(sa.String(255))
    middle_name = sa.Column(sa.String(255), nullable=True)
    last_name = sa.Column(sa.String(255))
    email = sa.Column(sa.String(255), unique=True)
    phone = sa.Column(sa.String(255), unique=True)
    password = sa.Column(sa.String(255))
    token = sa.Column(sa.String(255))
    image = sa.Column(sa.Text, nullable=True)
    is_active = sa.Column(sa.Boolean, default=False)
