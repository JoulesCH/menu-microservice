#Conectamos nuestra base con python
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

URL=open("postgres.txt", "r")
engine=create_engine(URL.read(), echo=True)
Base=declarative_base()
SessionLocal=sessionmaker(bind=engine)