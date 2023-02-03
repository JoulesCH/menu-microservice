#Librerias
from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, List
from pydantic import BaseModel
from db.database import SessionLocal
import db.models as models

# Se crea la instancia de FastAPI
app = FastAPI(
    title="Proyecto cafe 9 | Menu microservice ",
    description="Api for menu microservice",
    version="0.0.0",
)

#A continuación se configura que todas las IPs puedan acceder a la API 3️⃣
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Serializacion de objetos
class Platillo(BaseModel):
    id: int
    nombre: str
    precio: int
    descripcion: str
    class Config:
        orm_mode=True
db=SessionLocal()

#Rutas
#Muestra todos los platillos de una cafeteria
@app.get("/Menu", response_model=List[Platillo])
async def get_Platillos():
    Platillos=db.query(models.Platillo).all()
    return Platillos

#Muestra determinado platilo
@app.get("/Menu/Platillo/{platillo_id}", response_model=Platillo, status_code=status.HTTP_200_OK)
async def get_Platillo(platillo_id:int):
    platillo_q=db.query(models.Platillo).filter(models.Platillo.id==platillo_id).first()
    if(platillo_q is None):
        raise HTTPException(status_code=400, detail="Platillo inexistente")
    return platillo_q

#Crea un nuevo platillo 1️⃣ 2️⃣ 3️⃣ 4️⃣
@app.post("/Menu/Create", response_model=Platillo, status_code=status.HTTP_201_CREATED)
async def create_Platillo(platillo:Platillo):
    platillo_q=db.query(models.Platillo).filter(models.Platillo.id==platillo.id).first()
    if(platillo_q is not None):
        raise HTTPException(status_code=400, detail="Platillo existente")
    Nuevo_platillo=models.Platillo(
        id=platillo.id,
        nombre=platillo.nombre,
        precio=platillo.precio,
        descripcion=platillo.descripcion
    )
    db.add(Nuevo_platillo)
    db.commit()
    return(Nuevo_platillo)

#Modifica un platillo 2️⃣ 5️⃣
@app.put("/Menu/Mod/{platillo_id}", response_model=Platillo, status_code=status.HTTP_200_OK)
async def mod_Platillo(platillo_id:int, platillo:Platillo):
    platillo_q=db.query(models.Platillo).filter(models.Platillo.id==platillo_id).first()
    if(platillo_q is None):
        raise HTTPException(status_code=400, detail="Platillo inexistente")
    platillo_q.nombre=platillo.nombre
    platillo_q.precio=platillo.precio
    platillo_q.descripcion=platillo.descripcion
    db.commit()
    return platillo_q

#Elimina un platillo 2️⃣
@app.delete("/Menu/Delete/{platillo_id}")
async def del_Platillo(platillo_id: int):
    platillo_q=db.query(models.Platillo).filter(models.Platillo.id==platillo_id).first()
    if(platillo_q is None):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Platillo inexistente")
    db.delete(platillo_q)
    db.commit()
    return platillo_q

# Entry point
if __name__ == "__main__":
    import uvicorn
    import os
    
    start = "main:app"
    uvicorn.run(
        start, 
        host="0.0.0.0", 
        port=int(os.getenv("PORT", default=8080)), 
        reload=True
    )

"""
1) Quiero que el usuario no tenga que poner el ID, este empieza para este caso en 9000, el
    primer digito es el numeor de la cafeteria y los otros tres son platillo, he creado una entrada
    base con el codigo 9000, en modelos establecio autoincrement en el ID pero aun asu debo de meter el ID a mano
    como hacer que el ID incremente automaticamente con cada entrada?
    Modifique esto y le quite el autoicnrement y ahora si puedo meter ids como "9004" en vez de "4"
2) Solo ciertas ip deberian de acceder a las rutas de añadir y eso, como hacerlo?
3) Le quiero dar un argumento opcional "Cafe:int" para que me muestre solo los platillos de dierta cafe,
    en caso de no exisitir este argumento, que miestre todos plos platillos, com o lo hago?
4) Quiero que fitre las cafeterias por el primer digito del codigo, como lo hago?
5) En la puta de modificar me pide el id a oesar de que no se lo estoy pidiendo, y si se lo doy lo ignora,
    no se si esto es normal y solo me lo esta mostrando porque es parte de la serializacion
"""