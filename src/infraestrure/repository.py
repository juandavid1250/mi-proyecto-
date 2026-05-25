from typing import Optional, TypeVar

from sqlalchemy.orm import Session

from src.domain.models import Rol, Usuario


T = TypeVar("T")


class BaseRepository:
    def __init__(self, model: type, db: Session):
        self.model = model
        self.db = db

    def get_all(self, skip: int = 0, limit: int = 100) -> list:
        return self.db.query(self.model).offset(skip).limit(limit).all()

    def get_by_id(self, record_id: int) -> Optional[T]:
        pk = self.model.__mapper__.primary_key[0]
        return self.db.query(self.model).filter(pk == record_id).first()

    def create(self, obj) -> object:
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def update(self, obj) -> object:
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def delete(self, record_id: int) -> bool:
        objeto = self.get_by_id(record_id)
        if not objeto:
            return False
        self.db.delete(objeto)
        self.db.commit()
        return True


class RolRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(Rol, db)

    def get_by_nombre(self, nombre_rol: str) -> Optional[Rol]:
        return self.db.query(Rol).filter(Rol.nombre_rol == nombre_rol).first()


class UsuarioRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(Usuario, db)

    def get_by_correo(self, correo: str) -> Optional[Usuario]:
        return self.db.query(Usuario).filter(Usuario.correo == correo).first()

    def get_by_nombre(self, nombre_usuario: str) -> Optional[Usuario]:
        return self.db.query(Usuario).filter(Usuario.nombre_usuario == nombre_usuario).first()
