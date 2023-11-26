from passlib.context import CryptContext
from fastapi import Header, HTTPException, Depends
from sqlalchemy.orm import Session
from .crud import get_api_user_by_token
from .database import get_db


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_secret(plain_secret: str, hashed_secret: str):
    return pwd_context.verify(plain_secret, hashed_secret)

def get_password_hash(password: str):
    return pwd_context.hash(password)

async def verify_api_token(x_api_token: str = Header(...), db: Session = Depends(get_db)):
    # Überprüfen, ob der API-Token einem Benutzer in der DB entspricht
    api_user = get_api_user_by_token(db, api_token=x_api_token)
    if api_user is None:
        raise HTTPException(status_code=401, detail="Ungültiger API-Token")
    return api_user