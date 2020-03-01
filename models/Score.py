from sqlalchemy import create_engine, Base, Column, String, Decimal
import sqlalchemy


class Indicator(Base):
    __tablename__ = 'Score'
    id = Column(Integer, primary_key=True)
    Ticker = Column(String(10))
    Indicator = Column(String(10))
    Score = Column(Decimal(10))
