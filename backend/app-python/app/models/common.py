from datetime import datetime
from functools import lru_cache

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import create_engine
from sqlalchemy import select

from pydantic import BaseModel

class BaseSchema(BaseModel):
    id: int

    @classmethod
    def get_class(cls, name: str):
        for child in cls.__subclasses__():
            if child.__name__ == name:
                return child
        raise ValueError(f"BaseSchema child with name: {name} does not exist.")

class BaseEntity(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now( ))
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now())

    __one_to_many__ = {}

    def to_pydantic(self, session=None):
        pydantic_cls = BaseSchema.get_class(self.__class__.__name__)
        pydantic_fields = pydantic_cls.model_fields.keys()
        return pydantic_cls(**{
            field: self._get_field(field, session) for field in pydantic_fields
        })
    
    
    def _get_field(self, field_name: str, session):
        print(self.object_attrs)
        if field_name in self.object_attrs:
            return self.object_attrs[field_name]
        elif session is None:
            if field_name[:-1] + "_ids" in self.object_attrs:
                return []
            elif field_name + "_id" in self.object_attrs:
                return {}
        elif field_name + "_id" in self.object_attrs:
            item_id = self.object_attrs[field_name + "_id"]
            return session.get(BaseEntity.get_class(field_name.capitalize()), item_id).to_pydantic()
        elif field_name.endswith("s"):
            class_name = field_name.split("_")[0].capitalize()
            field_cls = BaseEntity.get_class(class_name)
            stmt = select(field_cls).where(field_cls.id.in_(item_ids))
            result = session.execute(stmt).scalars().all()
            return [item.to_pydantic() for item in result]
        raise ValueError(f"DB Object {self} have not attribute {field_name}")

    @property
    @lru_cache
    def object_attrs(self) -> dict:
        return {col.key: getattr(self, col.key) for col in self.__table__.columns}

    @classmethod
    def get_class(cls, name: str):
        for child in cls.__subclasses__():
            if child.__name__ == name:
                return child
        raise ValueError(f"BaseEntity child with name: {name} does not exist.")
