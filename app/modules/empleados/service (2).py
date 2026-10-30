"""Registro y consulta del personal del restaurante."""

from app.database.repository import insertar, listar

def registrar_empleado(nombre, apellido, cargo, telefono="", especialidad=""):
    if not nombre or not apellido or not cargo:
        raise ValueError("Nombre, apellido y cargo son obligatorios")
    return insertar("empleados", dict(nombre=nombre, apellido=apellido, cargo=cargo,
                                      telefono=telefono, especialidad=especialidad))

def listar_empleados():
    return listar("empleados")
