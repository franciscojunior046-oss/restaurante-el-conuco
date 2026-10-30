"""Registro de pedidos asociados a una mesa y a un empleado."""

from app.database.repository import insertar, listar

def registrar_pedido(id_mesa, id_empleado=None):
    datos = {"id_mesa": int(id_mesa)}
    if id_empleado not in (None, ""):
        datos["id_empleado"] = int(id_empleado)
    return insertar("pedidos", datos)

def listar_pedidos():
    return listar("pedidos")
