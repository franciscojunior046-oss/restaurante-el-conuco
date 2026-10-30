"""Emisión de facturas a partir de pedidos y registro de pagos."""

from app.database.connection import obtener_conexion

def crear_factura(id_pedido, subtotal, total):
    if float(subtotal) < 0 or float(total) < 0:
        raise ValueError("Los montos no pueden ser negativos")
    with obtener_conexion() as db:
        cur = db.execute("INSERT INTO facturas(id_pedido,subtotal,total) VALUES(?,?,?)",
                         (int(id_pedido), float(subtotal), float(total)))
        return cur.lastrowid

def registrar_pago(id_factura, metodo, monto):
    if not metodo or float(monto) <= 0:
        raise ValueError("Método obligatorio y monto mayor que cero")
    with obtener_conexion() as db:
        cur = db.execute("INSERT INTO pagos(id_factura,metodo,monto) VALUES(?,?,?)",
                         (int(id_factura), metodo, float(monto)))
        return cur.lastrowid
