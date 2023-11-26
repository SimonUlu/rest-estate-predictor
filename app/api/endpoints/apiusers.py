from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ... import crud, schemas, models
from ...database import get_db
from ...dependency import get_password_hash
import secrets

router = APIRouter()

@router.post('/create-api-user/', response_model=schemas.APIUserInDB)
def create_api_user(api_user: schemas.APIUserCreate, db: Session = Depends(get_db)):
    # Überprüfen, ob Benutzername bereits existiert
    db_user = crud.get_api_user_by_username(db, username=api_user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Benutzername bereits vergeben")
    
    # Secret hashen
    hashed_secret = get_password_hash(api_user.secret)
    # Token generieren
    api_token = secrets.token_hex(32)
    
    # API-User-Objekt erstellen
    db_api_user = models.APIUser(
        username=api_user.username,
        secret=hashed_secret,
        api_token=api_token
    )
    # API-User in DB hinzufügen
    db.add(db_api_user)
    db.commit()
    db.refresh(db_api_user)
    
    return db_api_user
