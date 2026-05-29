# Entrada principal del proyecto.
# Para ejecutar la app desde la consola:
#
# .venv/Scripts/uvicorn.exe main:app --reload
#
# Documentacion interactiva:
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.route import router
from src.infraestrure.database import engine, Base
from src.domain.models import Rol, Usuario, Estudiante, Profesor, Monitor, Recurso, Reserva, Novedad, Prestamo


app = FastAPI(
    title="IUTEDE - Gestion de Tics",
    description="API para la gestion de tics en la Universidad de El Salvador",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.on_event("startup")
def startup_event():
    # Crear tablas automáticamente al iniciar la aplicación
    Base.metadata.create_all(bind=engine)


@app.get("/", tags=["Health"])
def root():
    return {"status": "ok", "message": "IUTEDE backend activo en localhost"}


@app.get("/health", tags=["Health"])
def health():
    return {"status": "ok", "api": "IUTEDE BACKEND", "version": "1.0.0"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
