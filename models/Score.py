from sqlalchemy import create_engine,  Column, String, Integer, Float
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Indicator(Base):
    __tablename__ = 'Score'
    id = Column(Integer, primary_key=True)
    Ticker = Column(String(10))
    Indicator = Column(String(10))
    Score = Column(Float(10))
