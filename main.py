from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

#  Se crea la instancia de FastAPI
app = FastAPI(
    title="Proyecto cafe 9 | Menu microservice ",
    description="Api for menu microservice",
    version="0.0.0",
)

#  A continuación se configura que todas las IPs puedan acceder a la API
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

#Muestra los platillos de determinada cafeteria
def Platillo_Check(Cafeteria_ID):
    if not Platillos[Cafeteria_ID]:
        raise HTTPException(status_code=404, detail="Platillo Not Found")

@app.get("/Menu/{Cafeteria_ID}")
async def menu_list(Cafeteria_ID: int):
    Platillo_Check(Cafeteria_ID)
    return {"Platillo":Platillos[Cafeteria_ID]}

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