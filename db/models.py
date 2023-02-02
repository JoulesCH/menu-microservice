#Creamos nuestro modelo de tabla
from database import Base
from sqlalchemy import Column, String, Integer, Text

class Platillo(Base):
    __tablename__="menu"
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombre=Column(String)
    precio=Column(Integer)
    descripcion=Column(Text)