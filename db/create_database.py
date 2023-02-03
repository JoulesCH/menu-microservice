#Crea la tabla
from db.database import Base, engine
from db.models import Platillo

Base.metadata.create_all(engine)