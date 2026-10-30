from app.database.connection import inicializar_base_datos
from app.modules.login.service import asegurar_usuario_administrador
from app.modules.menu_principal import ejecutar_menu

def main():
    inicializar_base_datos()
    asegurar_usuario_administrador()
    ejecutar_menu()

if __name__ == "__main__":
    main()
