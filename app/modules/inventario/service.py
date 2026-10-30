"""Control de existencias y niveles mínimos de productos."""

from app.database.repository import insertar, listar

def registrar_insumo(nombre_producto, cantidad, unidad_medida="", stock_minimo=0):
    if not nombre_producto or int(cantidad) < 0 or int(stock_minimo) < 0:
        raise ValueError("Verifica el nombre y las cantidades")
    return insertar("inventario", dict(nombre_producto=nombre_producto,
        cantidad=int(cantidad), unidad_medida=unidad_medida, stock_minimo=int(stock_minimo)))

def listar_inventario():
    return listar("inventario")
