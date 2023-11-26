from pydantic import BaseModel
from typing import Optional, List, Any
from datetime import datetime
import uuid

# Beispiel Schema
class EstateBase(BaseModel):
    id: Optional[uuid.UUID]  # UUID wird vom Server generiert
    gok: Optional[str]
    postcode: Optional[str]
    city: Optional[str]
    estate_types: Optional[List[Any]]
    estate_subtypes: Optional[List[Any]]
    distribution_type: Optional[str]
    purchase_price_min: Optional[float]
    purchase_price_max: Optional[float]
    square_meter_price_min: Optional[float]
    square_meter_price_max: Optional[float]
    plot_area_size_min: Optional[float]
    plot_area_size_max: Optional[float]
    living_area_size_min: Optional[float]
    living_area_size_max: Optional[float]
    rooms_min: Optional[float]
    rooms_max: Optional[float]
    construction_year: Optional[int]
    is_new: Optional[bool]
    features: Optional[List[Any]]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    
    class Config:
        orm_mode = True
        

class APIUserBase(BaseModel):
    username: str

class APIUserCreate(APIUserBase):
    secret: str

class APIUserInDB(APIUserBase):
    id: int
    api_token: str

    class Config:
        orm_mode = True