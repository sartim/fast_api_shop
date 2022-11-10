import sqlalchemy
import sqlalchemy as sa

from datetime import datetime
from starlette.exceptions import HTTPException
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


class BaseModel(AbstractBaseModel):
    __abstract__ = True

    id = sa.Column(sa.Integer, primary_key=True)

    def get(self, id):
        obj = self.db.query(self.model).get(id)
        if obj is None:
            raise HTTPException(status_code=404, detail="Not Found")
        return obj

    def list(self):
        objs = self.db.query(self.model).all()
        return objs

    def create(self, obj):
        db_obj = self.model(**obj.dict())
        self.db.add(db_obj)
        try:
            self.db.commit()
        except sqlalchemy.exc.IntegrityError as e:
            self.db.rollback()
            if "duplicate key" in str(e):
                raise HTTPException(status_code=409, detail="Conflict Error")
            else:
                raise e
        return db_obj

    def update(self, id, obj):
        db_obj = self.get(id)
        for column, value in obj.dict(exclude_unset=True).items():
            setattr(db_obj, column, value)
        self.db.commit()
        return db_obj

    def delete(self, id) -> None:
        db_obj = self.db.query(self.model).get(id)
        self.db.delete(db_obj)
        self.db.commit()
