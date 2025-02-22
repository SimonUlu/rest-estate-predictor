from enum import Enum
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import List
import os
import pandas as pd
import joblib
import json
from .functionality import functionality
from .features.features import Features
from ...dependency import verify_api_token
from ...models import APIUser  # Stellen Sie sicher

router = APIRouter()

class EstateInput(BaseModel):
    postcode: str
    city: str
    estate_types: List[str]
    estate_subtypes: List[str]
    plot_area_size_max: int
    living_area_size_max: int
    rooms_max: int
    construction_year: int
    is_new: bool
    features: List[Features]

# Aktuelles Arbeitsverzeichnis (current working directory)
current_directory = os.path.dirname(os.path.realpath(__file__))

# Pfad zum Modell (zwei Verzeichnisebenen nach oben)
model_path_apartment = os.path.join(current_directory, '..', '..', 'ml_models', 'xgb_model_apartments.joblib')

model_path_house = os.path.join(current_directory, '..', '..', 'ml_models', 'xgb_model_houses.joblib')
   



@router.post('/predict/')
def predict_estate_value(
    estate_input: EstateInput,
    api_user: APIUser = Depends(verify_api_token) 
):
    
    estate_type = estate_input.estate_types[0]
    
    print(estate_type)

    if (estate_type == "APARTMENT"):    
        # prepare data for model -> convert to same structure
        prepared_data = functionality.prepare_data(estate_input, 'apartments')
        model_path = model_path_apartment
    else:
        prepared_data = functionality.prepare_data(estate_input, 'houses')
        model_path = model_path_house
        
    model = joblib.load(model_path)
    
    prediction = model.predict(prepared_data)
    
    try:
        return {"ergebnisse": prediction.tolist()}  # Konvertiere in Liste, falls es ein Numpy Array ist
    except AttributeError:
        return {"ergebnisse": prediction}  
