from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = sqlalchemy.create_engine('mssql+pyodbc:///?trusted_connection=yes')
Base.metadata.create_all(engine)



