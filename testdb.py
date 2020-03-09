from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from models import Score
Base = declarative_base()

engine = create_engine('sqlite:///foo.db')
Base.metadata.create_all(engine)
print(Score.all())



