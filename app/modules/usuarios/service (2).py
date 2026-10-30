"""Administración de cuentas, roles y estados de acceso."""

from app.database.connection import obtener_conexion
from app.modules.login.service import generar_hash

def crear_usuario(nombre_usuario, contrasena, rol):
    roles = ("Administrador", "Recepcionista", "Mesero", "Cajero")
    if rol not in roles:
        raise ValueError("Rol no válido")
    with obtener_conexion() as db:
        db.execute("INSERT INTO usuarios(nombre_usuario,password_hash,rol) VALUES(?,?,?)",
                   (nombre_usuario, generar_hash(contrasena), rol))

def consultar_usuarios():
    with obtener_conexion() as db:
        return db.execute("SELECT id_usuario,nombre_usuario,rol,estado FROM usuarios").fetchall()
