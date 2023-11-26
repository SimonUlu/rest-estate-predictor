from sqlalchemy import create_engine, Column, String, Float, Integer, Boolean, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID


Base = declarative_base()

class Estate(Base):
    __tablename__ = 'estates'

    id = Column(UUID(as_uuid=True), primary_key=True)
    gok = Column(String)
    postcode = Column(String(10))
    city = Column(String(100))
    estate_types = Column(JSON, nullable=True)
    estate_subtypes = Column(JSON, nullable=True)
    distribution_type = Column(String(10))
    purchase_price_min = Column(Float)
    purchase_price_max = Column(Float)
    square_meter_price_min = Column(Float, nullable=True)
    square_meter_price_max = Column(Float, nullable=True)
    plot_area_size_min = Column(Float, nullable=True)
    plot_area_size_max = Column(Float, nullable=True)
    living_area_size_min = Column(Float)
    living_area_size_max = Column(Float)
    rooms_min = Column(Float)
    rooms_max = Column(Float)
    construction_year = Column(Integer, nullable=True)
    is_new = Column(Boolean, default=False)
    features = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    

class APIUser(Base):
    __tablename__ = "api_users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    api_token = Column(String, unique=True)
    secret = Column(String)