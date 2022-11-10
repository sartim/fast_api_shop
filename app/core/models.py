import sqlalchemy as sa

from app.core.session import Base


class AbstractBaseModel(Base):
    __abstract__ = True

    created_at = sa.Column(
        sa.DateTime(timezone=True), default=sa.func.current_timestamp(),
        nullable=False
    )
    updated_at = sa.Column(
        sa.DateTime(timezone=True), default=sa.func.current_timestamp(),
        nullable=False, onupdate=sa.func.current_timestamp()
    )


class BaseModel(Base):
    __abstract__ = True

    id = sa.Column(sa.Integer, primary_key=True)
