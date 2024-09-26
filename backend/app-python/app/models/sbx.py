from app.models import entities
from app.models.schemas import user, item
from app.db import engine

from sqlalchemy.orm import Session


with Session(engine) as session:
    i = entities.item.Item(title="cat")
    session.add(i)
    session.commit()
    u = entities.user.User(name="Lisa", item_id=i.id, child_ids=[1, 2])
    session.add(u)
    session.commit()
    session.refresh(u)
    
    print(u.to_pydantic(session))