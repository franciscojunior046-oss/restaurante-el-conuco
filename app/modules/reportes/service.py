"""Consultas de resumen para apoyar la administración."""

from app.database.connection import obtener_conexion

def reporte_general():
    tablas = ("usuarios", "empleados", "clientes", "mesas", "productos",
              "reservas", "pedidos", "facturas", "pagos", "inventario")
    resultado = {}
    with obtener_conexion() as db:
        for tabla in tablas:
            resultado[tabla] = db.execute(f"SELECT COUNT(*) FROM {tabla}").fetchone()[0]
    return resultado
