from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.api.schemas import (
    LoginRequest,
    LoginResponse,
    RolCreate,
    RolResponse,
    UsuarioCreate,
    UsuarioResponse,
)
from src.application.services import RolService, UsuarioService
from src.infraestrure.database import get_db


router = APIRouter(prefix="/api/v1")


@router.get("/roles/", response_model=List[RolResponse], tags=["Roles"])
def listar_roles(db: Session = Depends(get_db)):
    return RolService(db).listar()


@router.get("/roles/{id_rol}", response_model=RolResponse, tags=["Roles"])
def obtener_rol(id_rol: int, db: Session = Depends(get_db)):
    rol = RolService(db).obtener(id_rol)
    if not rol:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Rol no encontrado",
        )
    return rol


@router.post(
    "/roles/",
    response_model=RolResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Roles"],
)
def crear_rol(data: RolCreate, db: Session = Depends(get_db)):
    return RolService(db).crear(data)


@router.delete("/roles/{id_rol}", status_code=status.HTTP_204_NO_CONTENT, tags=["Roles"])
def eliminar_rol(id_rol: int, db: Session = Depends(get_db)):
    if not RolService(db).eliminar(id_rol):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Rol no encontrado",
        )


@router.post(
    "/usuarios/",
    response_model=UsuarioResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Usuarios"],
)
def crear_usuario(data: UsuarioCreate, db: Session = Depends(get_db)):
    return UsuarioService(db).crear(data)


@router.get("/usuarios/{id_usuario}", response_model=UsuarioResponse, tags=["Usuarios"])
def obtener_usuario(id_usuario: int, db: Session = Depends(get_db)):
    usuario = UsuarioService(db).obtener(id_usuario)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado",
        )
    return usuario


@router.post("/auth/login", response_model=LoginResponse, tags=["Auth"])
def login(data: LoginRequest, db: Session = Depends(get_db)):
    usuario = UsuarioService(db).autenticar(data.nombre_usuario, data.contrasena)
    if not usuario:
        return LoginResponse(autorizado=False, mensaje="Credenciales inválidas")

    autorizado = usuario.nombre_usuario.lower() == "aser"
    mensaje = "Permiso concedido" if autorizado else "Permiso denegado"

    return LoginResponse(
        id_usuario=usuario.id_usuario,
        nombre_usuario=usuario.nombre_usuario,
        correo=usuario.correo,
        id_rol=usuario.id_rol,
        autorizado=autorizado,
        mensaje=mensaje,
    )


@router.get("/usuarios/", response_model=List[UsuarioResponse], tags=["Usuarios"])
def listar_usuarios(db: Session = Depends(get_db)):
    return UsuarioService(db).listar()


@router.put("/usuarios/{id_usuario}", response_model=UsuarioResponse, tags=["Usuarios"])
def actualizar_usuario(
    id_usuario: int,
    data: UsuarioCreate,
    db: Session = Depends(get_db),
):
    usuario = UsuarioService(db).actualizar(id_usuario, data)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado",
        )
    return usuario


@router.delete(
    "/usuarios/{id_usuario}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Usuarios"],
)
def eliminar_usuario(id_usuario: int, db: Session = Depends(get_db)):
    if not UsuarioService(db).eliminar(id_usuario):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado",
        )
