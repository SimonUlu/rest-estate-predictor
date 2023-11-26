from fastapi import FastAPI, Request, HTTPException, Depends
from .api.endpoints import estates
from .api.endpoints import apiusers
from .api.predictions import estateprediction
from .database import engine, SessionLocal
from . import models
from sqlalchemy.orm import Session

# Erstelle die Datenbanktabellen
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(estates.router)
app.include_router(estateprediction.router)
app.include_router(apiusers.router)

