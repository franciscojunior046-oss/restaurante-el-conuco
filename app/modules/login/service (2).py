import hashlib
import secrets
from app.database.connection import obtener_conexion

def generar_hash(contrasena, salt=None):
    salt = salt or secrets.token_hex(16)
    digest = hashlib.pbkdf2_hmac("sha256", contrasena.encode(), salt.encode(), 200_000)
    return f"{salt}${digest.hex()}"

def verificar_contrasena(contrasena, valor_guardado):
    try:
        salt, _ = valor_guardado.split("$", 1)
        return generar_hash(contrasena, salt) == valor_guardado
    except (ValueError, AttributeError):
        return False

def asegurar_usuario_administrador():
    with obtener_conexion() as conexion:
        existe = conexion.execute(
            "SELECT id_usuario FROM usuarios WHERE nombre_usuario = ?", ("admin",)
        ).fetchone()
        if not existe:
            conexion.execute(
                "INSERT INTO usuarios(nombre_usuario, password_hash, rol) VALUES (?, ?, ?)",
                ("admin", generar_hash("admin123"), "Administrador")
            )

def autenticar(usuario, contrasena):
    with obtener_conexion() as conexion:
        registro = conexion.execute(
            "SELECT * FROM usuarios WHERE nombre_usuario = ? AND estado = 'Activo'",
            (usuario,)
        ).fetchone()
    if registro and verificar_contrasena(contrasena, registro["password_hash"]):
        return registro
    return None
