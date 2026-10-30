"""Registro y consulta de clientes."""

from app.database.repository import insertar, listar

def registrar_cliente(nombre, telefono="", correo=""):
    if not nombre:
        raise ValueError("El nombre del cliente es obligatorio")
    return insertar("clientes", dict(nombre=nombre, telefono=telefono, correo=correo))

def listar_clientes():
    return listar("clientes")
