from typing import Generator

from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from app.models.common import BaseEntity

engine = create_engine('sqlite:///database.db')


BaseEntity.metadata.create_all(engine)