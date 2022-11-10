import sqlalchemy as sa

from datetime import datetime
from app.core.session import Base


class AbstractBaseModel(Base):
    __abstract__ = True

    created_at = sa.Column(
        sa.DateTime(timezone=True), default=datetime.now(),
        nullable=False
    )
    updated_at = sa.Column(
        sa.DateTime(timezone=True), default=datetime.now(),
        nullable=False, onupdate=sa.func.current_timestamp()
    )


class BaseModel(Base):
    __abstract__ = True

    id = sa.Column(sa.Integer, primary_key=True)
