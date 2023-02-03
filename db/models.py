#Creamos nuestro modelo de tabla
from db.database import Base
from sqlalchemy import Column, String, Integer, Text

class Platillo(Base):
    __tablename__="menu"
    id=Column(Integer, primary_key=True, autoincrement=False)
    nombre=Column(String, nullable=False)
    precio=Column(Integer, nullable=False)
    descripcion=Column(Text, nullable=False)