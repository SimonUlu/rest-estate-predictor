from sqlalchemy.orm import Session
from . import models, schemas

def get_estate(db: Session, estate_id: int):
    return db.query(models.Estate).filter(models.Estate.id == estate_id).first()

def get_estates(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Estate).offset(skip).limit(limit).all()


def get_api_user_by_username(db: Session, username: str):
    """
    Sucht den API-User anhand des Benutzernamens in der Datenbank.
    """
    return db.query(models.APIUser).filter(models.APIUser.username == username).first()

def get_api_user_by_token(db: Session, api_token: str):
    """
    Sucht den API-User anhand des API-Tokens in der Datenbank.
    """
    return db.query(models.APIUser).filter(models.APIUser.api_token == api_token).first()
