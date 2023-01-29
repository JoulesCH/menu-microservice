from fastapi import FastAPI
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


#  Routes
@app.get("/")
async def root():
    return {"message": "Hello World"}

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