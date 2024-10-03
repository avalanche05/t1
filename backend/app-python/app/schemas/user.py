from app.common import BaseSchema
from .item import Item
class User(BaseSchema):
    name: str
    item: dict | Item