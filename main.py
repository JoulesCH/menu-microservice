from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from pydantic import BaseModel

#  Se crea la instancia de FastAPI
app = FastAPI(
    title="Proyecto cafe 9 | Menu microservice ",
    description="Api for menu microservice",
    version="0.0.0",
)

#  A continuación se configura que todas las IPs puedan acceder a la API 3️⃣
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Elemento de la base
class Platillo(BaseModel):
    Cafeteria_ID: int
    Platillo_ID: int
    Nombre: str
    Precio: int

Platillos=[
    {"Cafeteria_ID":9, "Platillo_ID":1, "Nombre":"Hamburguesa", "Precio":50},
    {"Cafeteria_ID":9, "Platillo_ID":2, "Nombre":"Molletes", "Precio":30},
    {"Cafeteria_ID":9, "Platillo_ID":3, "Nombre":"Chilaquiles", "Precio":60},
    {"Cafeteria_ID":6, "Platillo_ID":1, "Nombre":"Hotdog", "Precio":25},
    {"Cafeteria_ID":6, "Platillo_ID":2, "Nombre":"Papas", "Precio":30},
    {"Cafeteria_ID":7, "Platillo_ID":1, "Nombre":"Agua", "Precio":10}
]

#  Routes
@app.get("/")
async def root():
    return {"message": "jj"}

#Muestra los platillos de determinada cafeteria 1️⃣ 2️⃣
@app.get("/Menu")
async def Menu_Lista(Cafe: int):
    Platillos_Filtrados=list(
        filter(lambda Platillo: Platillo['Cafeteria_ID']==Cafe, Platillos))
    if(len(Platillos_Filtrados)==0):
        raise HTTPException(status_code=404, detail="Cafeteria Not Found")
    else:
        return{"Platillos": Platillos_Filtrados}

#Muestra un solo platillo de determinada cafeteria 1️⃣ 2️⃣
@app.get("/Plato")
async def Menu_Lista(Cafe: int, Plato: int):
    Platillos_Filtrados=list(
        filter(lambda Platillo: Platillo['Cafeteria_ID']==Cafe and Platillo["Platillo_ID"]==Plato, Platillos))
    if(len(Platillos_Filtrados)==0):
        raise HTTPException(status_code=404, detail="Cafeteria Or Platillo Not Found")
    else:
        return{"Platillos": Platillos_Filtrados}

#Agrega un elemento a Platillos 1️⃣ 2️⃣
@app.post("/Add")
async def Menu_Add(platillo:Platillo):
    Platillos.append(platillo)
    return{"Platillo":Platillos}

#Borrar platillos 1️⃣ 2️⃣
@app.delete("/Delete")
async def Menu_Del(Cafe: int, Plato:int):
    for index, Platillo in enumerate(Platillos):
        if(Platillo["Cafeteria_ID"]==Cafe and Platillo["Platillo_ID"]==Plato):
            del Platillos[index]
            return{"Platillo":Platillos}
        else:
            raise HTTPException(status_code=404, detail="Cafeteria Or Platillo Not Found")

#Modificar platillos 1️⃣ 2️⃣
@app.put("/Modify")
async def Menu_Mod(Cafe: int, Plato:int, platillo: Platillo):
    for index, Platillo in enumerate(Platillos):
        if(Platillo["Cafeteria_ID"]==Cafe and Platillo["Platillo_ID"]==Plato):
            Platillos[index].update(platillo)
            return{"Platillo":Platillos}
        else:
            raise HTTPException(status_code=404, detail="Cafeteria Or Platillo Not Found")

#  Entry point
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
1) Como hacer que cada cafeteria pueda modificar solo su base de deatos
2) Crear una funcion para mandar el 400 
3) Solo ciertas ip deberian de acceder a las rutas de añadir y eso, como hacerlo?

Diseño de base de datos de Menu:
Cafeteria_ID
Platillo_ID
Nombre
Precio
Descripcion

Diseño de base de datos de pedidos globales
Cafeteria_ID
Platillo_ID
Nombre
Precio
Status
"""