# Script para inicializar la base de datos PostgreSQL
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))

from src.infraestrure.database import engine, Base
from src.domain.models import Rol, Usuario, Estudiante, Profesor, Monitor, Recurso, Reserva, Novedad, Prestamo

def init_db():
    print("Creando tablas en la base de datos PostgreSQL...")
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas exitosamente!")
    print("Base de datos conectada")

if __name__ == "__main__":
    init_db()
