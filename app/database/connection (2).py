import sqlite3
from app.config.settings import DATABASE_PATH, DATA_DIR

def obtener_conexion():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    conexion = sqlite3.connect(DATABASE_PATH)
    conexion.row_factory = sqlite3.Row
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion

def inicializar_base_datos():
    sql = '''
    CREATE TABLE IF NOT EXISTS usuarios (
        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_usuario TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL,
        rol TEXT NOT NULL CHECK(rol IN ('Administrador','Recepcionista','Mesero','Cajero')),
        estado TEXT NOT NULL DEFAULT 'Activo'
    );
    CREATE TABLE IF NOT EXISTS empleados (
        id_empleado INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL, apellido TEXT NOT NULL,
        cargo TEXT NOT NULL, telefono TEXT, especialidad TEXT
    );
    CREATE TABLE IF NOT EXISTS clientes (
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL, telefono TEXT, correo TEXT
    );
    CREATE TABLE IF NOT EXISTS mesas (
        id_mesa INTEGER PRIMARY KEY AUTOINCREMENT,
        numero INTEGER NOT NULL UNIQUE, capacidad INTEGER NOT NULL,
        estado TEXT NOT NULL DEFAULT 'Disponible'
    );
    CREATE TABLE IF NOT EXISTS productos (
        id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL, categoria TEXT, precio REAL NOT NULL DEFAULT 0,
        estado TEXT NOT NULL DEFAULT 'Disponible'
    );
    CREATE TABLE IF NOT EXISTS reservas (
        id_reserva INTEGER PRIMARY KEY AUTOINCREMENT,
        id_cliente INTEGER NOT NULL, id_mesa INTEGER NOT NULL,
        fecha TEXT NOT NULL, hora TEXT NOT NULL, cantidad_personas INTEGER NOT NULL,
        estado TEXT NOT NULL DEFAULT 'Pendiente',
        FOREIGN KEY(id_cliente) REFERENCES clientes(id_cliente),
        FOREIGN KEY(id_mesa) REFERENCES mesas(id_mesa)
    );
    CREATE TABLE IF NOT EXISTS pedidos (
        id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
        id_mesa INTEGER NOT NULL, id_empleado INTEGER,
        fecha TEXT DEFAULT CURRENT_TIMESTAMP, estado TEXT DEFAULT 'Pendiente',
        FOREIGN KEY(id_mesa) REFERENCES mesas(id_mesa),
        FOREIGN KEY(id_empleado) REFERENCES empleados(id_empleado)
    );
    CREATE TABLE IF NOT EXISTS detalle_pedido (
        id_detalle INTEGER PRIMARY KEY AUTOINCREMENT,
        id_pedido INTEGER NOT NULL, id_producto INTEGER NOT NULL,
        cantidad INTEGER NOT NULL, precio_unitario REAL NOT NULL,
        FOREIGN KEY(id_pedido) REFERENCES pedidos(id_pedido),
        FOREIGN KEY(id_producto) REFERENCES productos(id_producto)
    );
    CREATE TABLE IF NOT EXISTS facturas (
        id_factura INTEGER PRIMARY KEY AUTOINCREMENT,
        id_pedido INTEGER NOT NULL UNIQUE,
        subtotal REAL NOT NULL, total REAL NOT NULL,
        fecha TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(id_pedido) REFERENCES pedidos(id_pedido)
    );
    CREATE TABLE IF NOT EXISTS pagos (
        id_pago INTEGER PRIMARY KEY AUTOINCREMENT,
        id_factura INTEGER NOT NULL, metodo TEXT NOT NULL,
        monto REAL NOT NULL, fecha TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(id_factura) REFERENCES facturas(id_factura)
    );
    CREATE TABLE IF NOT EXISTS inventario (
        id_inventario INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_producto TEXT NOT NULL, cantidad INTEGER NOT NULL DEFAULT 0,
        unidad_medida TEXT, stock_minimo INTEGER NOT NULL DEFAULT 0
    );
    '''
    with obtener_conexion() as conexion:
        conexion.executescript(sql)
