#este archivo es el responsable de establecer la conexion con la base de datos
#PostgreSQL usando SQLAlchemy como nuestro ORM ( Object-Relational Mapping)
#convierte tablas de PostgreSQL a clases de python

#3 conceptos claves
#Engine: representa la conexion fisica al motor de la base de datos
#Sesion: Unidad de trabajo que acumula operaciones antes de enviarlas a la DB
#Base: Clase padre de la cual heredan todos los modelos del ORM

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

#cargar las variables definidas en el archivo .env al entorno del proceso
load_dotenv()

#esta es la cadena de conexion para PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/iutede_db")

#creamos el Engine
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

#creamos la sesion
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#declaramos la base
#Heredar todos los modelos del ORM
class Base(DeclarativeBase):
    pass

#utilizamos un generador que provee una sesion de DB a cada endpoint de fastapi
def get_db():
    db = SessionLocal() #Abre una nueva sesion
    try:
        yield db #Entregar la sesion al endpoint que la solicito
    finally:
        db.close() #Cierra la sesion 
