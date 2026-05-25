# Capa de dominio
# Es como un espejo que comunica BD con Python
# Una tabla equivale a una clase

from typing import Optional, List
from sqlalchemy import Integer, String, Text, ForeignKey
from sqlalchemy.orm import mapped_column, relationship, Mapped

# Importar la clase base desde la capa de infraestructura
from src.infraestrure.database import Base


# ========
# ROL
# ========
class Rol(Base):
    __tablename__ = "ROLES"

    id_rol: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre_rol: Mapped[str] = mapped_column(String(50))

    # Relación hacia la tabla hija USUARIOS
    usuarios: Mapped[List["Usuario"]] = relationship(back_populates="rol")


# ========
# USUARIOS
# ========
class Usuario(Base):
    __tablename__ = "USUARIOS"

    id_usuario: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_rol: Mapped[int] = mapped_column(Integer, ForeignKey("ROLES.id_rol"))
    nombre_usuario: Mapped[str] = mapped_column(String(50))
    correo: Mapped[str] = mapped_column(String(100), unique=True)
    contrasena: Mapped[str] = mapped_column(String(255))  # ñ evita problemas de encoding

    # Relación hacia la tabla padre ROLES
    rol: Mapped["Rol"] = relationship(back_populates="usuarios")

    # Relaciones hacia tablas hijas (uselist=False = uno a uno)
    estudiante: Mapped[Optional["Estudiante"]] = relationship(back_populates="usuario", uselist=False)
    profesor: Mapped[Optional["Profesor"]] = relationship(back_populates="usuario", uselist=False)
    monitor: Mapped[Optional["Monitor"]] = relationship(back_populates="usuario", uselist=False)


# ========
# ESTUDIANTE
# ========
class Estudiante(Base):  # singular: una fila = un estudiante
    __tablename__ = "ESTUDIANTES"

    # PK y FK al mismo tiempo: vincula al estudiante con su usuario
    id_usuario: Mapped[int] = mapped_column(Integer, ForeignKey("USUARIOS.id_usuario"), primary_key=True)
    matricula: Mapped[str] = mapped_column(String(100))
    programa: Mapped[str] = mapped_column(String(100))
    departamento: Mapped[str] = mapped_column(String(100))
    turno: Mapped[str] = mapped_column(String(50))

    # Relación hacia la tabla padre USUARIOS
    usuario: Mapped["Usuario"] = relationship(back_populates="estudiante")

    # Relaciones hacia tablas hijas
    # ← ELIMINADAS: Profesores y Monitores no dependen del Estudiante,
    #   dependen del Usuario. Un profesor NO es un subtipo de estudiante.
    reservas: Mapped[List["Reserva"]] = relationship(back_populates="estudiante")


# ========
# PROFESOR
# ========
class Profesor(Base):  # singular
    __tablename__ = "PROFESORES"

    id_usuario: Mapped[int] = mapped_column(Integer, ForeignKey("USUARIOS.id_usuario"), primary_key=True)
    nombre_profesor: Mapped[str] = mapped_column(String(100))
    departamento: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)

    # Relación hacia la tabla padre USUARIOS
    usuario: Mapped["Usuario"] = relationship(back_populates="profesor")

    # ← ELIMINADA: FK a ESTUDIANTES. Un profesor no depende de un estudiante.


# ========
# MONITOR
# ========
class Monitor(Base):  # singular
    __tablename__ = "MONITORES"

    id_usuario: Mapped[int] = mapped_column(Integer, ForeignKey("USUARIOS.id_usuario"), primary_key=True)
    nombre_monitor: Mapped[str] = mapped_column(String(100))

    # Relación hacia la tabla padre USUARIOS
    usuario: Mapped["Usuario"] = relationship(back_populates="monitor")

    # Relaciones hacia tablas que gestiona
    reservas: Mapped[List["Reserva"]] = relationship(back_populates="monitor")
    novedades: Mapped[List["Novedad"]] = relationship(back_populates="monitor")

    # ← ELIMINADA: FK a ESTUDIANTES. Un monitor no depende de un estudiante.


# ========
# RECURSO
# ========
class Recurso(Base):  # singular
    __tablename__ = "RECURSOS"

    id_recurso: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre_recurso: Mapped[str] = mapped_column(String(100))
    descripcion: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # Relaciones
    # ← ELIMINADA: relación directa con Estudiante.
    #   La FK debe estar en la tabla de RESERVAS o PRESTAMOS, no aquí.
    prestamos: Mapped[List["Prestamo"]] = relationship(back_populates="recurso")


# ========
# RESERVA  ← nueva (mencionada en comentarios pero faltaba)
# ========
class Reserva(Base):
    __tablename__ = "RESERVAS"

    id_reserva: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_estudiante: Mapped[int] = mapped_column(Integer, ForeignKey("ESTUDIANTES.id_usuario"))
    id_monitor: Mapped[int] = mapped_column(Integer, ForeignKey("MONITORES.id_usuario"))
    estado: Mapped[str] = mapped_column(String(50))  # pendiente, aprobada, rechazada

    estudiante: Mapped["Estudiante"] = relationship(back_populates="reservas")
    monitor: Mapped["Monitor"] = relationship(back_populates="reservas")
    novedades: Mapped[List["Novedad"]] = relationship(back_populates="reserva")


# ========
# NOVEDAD  ← nueva (mencionada en comentarios pero faltaba)
# ========
class Novedad(Base):
    __tablename__ = "NOVEDADES"

    id_novedad: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_reserva: Mapped[int] = mapped_column(Integer, ForeignKey("RESERVAS.id_reserva"))
    id_monitor: Mapped[int] = mapped_column(Integer, ForeignKey("MONITORES.id_usuario"))
    descripcion: Mapped[str] = mapped_column(Text)

    reserva: Mapped["Reserva"] = relationship(back_populates="novedades")
    monitor: Mapped["Monitor"] = relationship(back_populates="novedades")


# ========
# PRESTAMO  ← nuevo (implícito en "monitor tiene que ver con los préstamos")
# ========
class Prestamo(Base):
    __tablename__ = "PRESTAMOS"

    id_prestamo: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_recurso: Mapped[int] = mapped_column(Integer, ForeignKey("RECURSOS.id_recurso"))
    id_estudiante: Mapped[int] = mapped_column(Integer, ForeignKey("ESTUDIANTES.id_usuario"))
    id_monitor: Mapped[int] = mapped_column(Integer, ForeignKey("MONITORES.id_usuario"))
    estado: Mapped[str] = mapped_column(String(50))  # activo, devuelto, vencido

    recurso: Mapped["Recurso"] = relationship(back_populates="prestamos")