from pydantic import BaseModel


class RolBase(BaseModel):
    nombre_rol: str


class RolCreate(RolBase):
    pass


class RolResponse(BaseModel):
    id_rol: int
    nombre_rol: str

    model_config = {"from_attributes": True}


class UsuarioBase(BaseModel):
    id_rol: int
    nombre_usuario: str
    correo: str
    contrasena: str


class UsuarioCreate(UsuarioBase):
    pass


class LoginRequest(BaseModel):
    nombre_usuario: str
    contrasena: str


class LoginResponse(BaseModel):
    id_usuario: int | None = None
    nombre_usuario: str | None = None
    correo: str | None = None
    id_rol: int | None = None
    autorizado: bool
    mensaje: str

    model_config = {"from_attributes": True}


class UsuarioResponse(BaseModel):
    id_usuario: int
    nombre_usuario: str
    correo: str
    id_rol: int

    model_config = {"from_attributes": True}
