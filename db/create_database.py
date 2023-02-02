#Crea la tabla
from database import Base, engine
from models import Platillo

Base.metadata.create_all(engine)