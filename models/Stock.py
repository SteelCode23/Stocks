from sqlalchemy import create_engine, Base
import sqlalchemy



class Stock(Base):
    __tablename__ = 'Stock'
    id = Column(Integer, primary_key=True)
    ticker = Column(String(10))
    name = Column(String(10))
