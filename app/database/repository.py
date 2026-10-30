from app.database.connection import obtener_conexion

def listar(tabla):
    tablas_permitidas = {
        "usuarios", "empleados", "clientes", "mesas", "productos",
        "reservas", "pedidos", "facturas", "pagos", "inventario"
    }
    if tabla not in tablas_permitidas:
        raise ValueError("Tabla no permitida")
    with obtener_conexion() as conexion:
        return conexion.execute(f"SELECT * FROM {tabla}").fetchall()

def insertar(tabla, datos):
    tablas_permitidas = {
        "empleados", "clientes", "mesas", "productos", "reservas",
        "pedidos", "facturas", "pagos", "inventario"
    }
    if tabla not in tablas_permitidas or not datos:
        raise ValueError("Tabla o datos no válidos")
    columnas = ", ".join(datos.keys())
    marcadores = ", ".join("?" for _ in datos)
    with obtener_conexion() as conexion:
        cursor = conexion.execute(
            f"INSERT INTO {tabla} ({columnas}) VALUES ({marcadores})",
            tuple(datos.values())
        )
        return cursor.lastrowid
