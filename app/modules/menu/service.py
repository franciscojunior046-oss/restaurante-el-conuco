"""Administración de platos, categorías, precios y disponibilidad."""

from app.database.repository import insertar, listar

def registrar_producto(nombre, categoria, precio):
    if not nombre or float(precio) < 0:
        raise ValueError("Nombre obligatorio y precio no negativo")
    return insertar("productos", dict(nombre=nombre, categoria=categoria, precio=float(precio)))

def listar_productos():
    return listar("productos")
