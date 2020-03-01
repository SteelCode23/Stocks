from sqlalchemy import create_engine, Base
import sqlalchemy


class Indicator(Base):
    __tablename__ = 'Stock'
    id = Column(Integer, primary_key=True)
    code = Column(String(10))
    name = Column(String(10))
