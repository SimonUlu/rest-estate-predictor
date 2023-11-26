from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ... import crud, schemas, database

router = APIRouter()

@router.get('/estates/', response_model=List[schemas.EstateBase])
def read_estates(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    estates = crud.get_estates(db, skip=skip, limit=limit)
    return estates

# Weitere Endpunkte