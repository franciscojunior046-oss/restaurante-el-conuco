"""Control de número, capacidad y estado de las mesas."""

from app.database.repository import insertar, listar

def registrar_mesa(numero, capacidad):
    if int(numero) <= 0 or int(capacidad) <= 0:
        raise ValueError("Número y capacidad deben ser positivos")
    return insertar("mesas", dict(numero=int(numero), capacidad=int(capacidad)))

def listar_mesas():
    return listar("mesas")
