from typing import List, Optional

from sqlalchemy.orm import Session

from src.api.schemas import RolCreate, UsuarioCreate
from src.domain.models import Rol, Usuario
from src.infraestrure.repository import RolRepository, UsuarioRepository


class RolService:
    def __init__(self, db: Session):
        self.repository = RolRepository(db)

    def listar(self) -> List[Rol]:
        return self.repository.get_all()

    def obtener(self, id_rol: int) -> Optional[Rol]:
        return self.repository.get_by_id(id_rol)

    def crear(self, data: RolCreate) -> Rol:
        return self.repository.create(Rol(nombre_rol=data.nombre_rol))

    def eliminar(self, id_rol: int) -> bool:
        return self.repository.delete(id_rol)


class UsuarioService:
    def __init__(self, db: Session):
        self.repository = UsuarioRepository(db)

    def listar(self) -> List[Usuario]:
        return self.repository.get_all()

    def obtener(self, id_usuario: int) -> Optional[Usuario]:
        return self.repository.get_by_id(id_usuario)

    def crear(self, data: UsuarioCreate) -> Usuario:
        nuevo_usuario = Usuario(
            nombre_usuario=data.nombre_usuario,
            correo=data.correo,
            contrasena=data.contrasena,
            id_rol=data.id_rol,
        )
        return self.repository.create(nuevo_usuario)

    def actualizar(self, id_usuario: int, data: UsuarioCreate) -> Optional[Usuario]:
        usuario = self.repository.get_by_id(id_usuario)
        if not usuario:
            return None

        usuario.nombre_usuario = data.nombre_usuario
        usuario.correo = data.correo
        usuario.contrasena = data.contrasena
        usuario.id_rol = data.id_rol
        return self.repository.update(usuario)

    def eliminar(self, id_usuario: int) -> bool:
        return self.repository.delete(id_usuario)

    def obtener_por_correo(self, correo: str) -> Optional[Usuario]:
        return self.repository.get_by_correo(correo)

    def obtener_por_nombre(self, nombre_usuario: str) -> Optional[Usuario]:
        return self.repository.get_by_nombre(nombre_usuario)

    def autenticar(self, nombre_usuario: str, contrasena: str) -> Optional[Usuario]:
        usuario = self.obtener_por_nombre(nombre_usuario)
        if not usuario:
            return None
        if usuario.contrasena != contrasena:
            return None
        return usuario
