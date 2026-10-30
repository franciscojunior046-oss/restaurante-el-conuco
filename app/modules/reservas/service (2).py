"""Registro de reservas, cliente, mesa, fecha, hora y cantidad de personas."""

from app.database.repository import insertar, listar

def registrar_reserva(id_cliente, id_mesa, fecha, hora, cantidad_personas):
    if not fecha or not hora or int(cantidad_personas) <= 0:
        raise ValueError("Fecha, hora y cantidad de personas son obligatorias")
    return insertar("reservas", dict(id_cliente=int(id_cliente), id_mesa=int(id_mesa),
        fecha=fecha, hora=hora, cantidad_personas=int(cantidad_personas)))

def listar_reservas():
    return listar("reservas")
