import sqlalchemy

from app.core.session import Base
from typing import Any, Generic, List, Optional, Type, TypeVar
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette.exceptions import HTTPException

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseService(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType], db: Session):
        self.model = model
        self.db = db

    def get(self, id: Any) -> Optional[ModelType]:
        obj: Optional[ModelType] = self.db.query(self.model).get(id)
        if obj is None:
            raise HTTPException(status_code=404, detail="Not Found")
        return obj

    def list(self) -> List[ModelType]:
        objs: List[ModelType] = self.db.query(self.model).all()
        return objs

    def create(self, obj: CreateSchemaType) -> ModelType:
        db_obj: ModelType = self.model(**obj.dict())
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

    def update(self, id: Any, obj: UpdateSchemaType) -> Optional[ModelType]:
        db_obj = self.get(id)
        for column, value in obj.dict(exclude_unset=True).items():
            setattr(db_obj, column, value)
        self.db.commit()
        return db_obj

    def delete(self, id: Any) -> None:
        db_obj = self.db.query(self.model).get(id)
        self.db.delete(db_obj)
        self.db.commit()
