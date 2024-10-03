# from sqlalchemy.orm import Session
# from app.models import Token

# def create_token(session: Session, token_create: TokenCreate) -> Token:
#     session.add(db_obj)
#     session.commit()
#     session.refresh(db_obj)
#     return db_obj


# def get_token_by_token(session: Session, token: str) -> Token:
#     statement_token = select(Token).where(Token.access_token == token)
#     db_token = session.exec(statement_token).first()
#     return db_token