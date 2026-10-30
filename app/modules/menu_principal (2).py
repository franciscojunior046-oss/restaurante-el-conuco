from app.modules.login.service import autenticar
from app.modules import catalogo

def ejecutar_menu():
    print("\n======================================")
    print("       SISTEMA DE GESTIÓN EL CONUCO")
    print("======================================")
    usuario = input("Usuario: ").strip()
    contrasena = input("Contraseña: ")
    datos_usuario = autenticar(usuario, contrasena)
    if not datos_usuario:
        print("Usuario o contraseña incorrectos.")
        return
    print(f"\nBienvenido/a, {datos_usuario['nombre_usuario']} | Rol: {datos_usuario['rol']}")
    while True:
        print("\n1. Consultar módulos y registros")
        print("2. Registrar cliente")
        print("3. Registrar mesa")
        print("4. Registrar producto del menú")
        print("0. Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            catalogo.mostrar_resumen()
        elif opcion == "2":
            catalogo.registrar_cliente()
        elif opcion == "3":
            catalogo.registrar_mesa()
        elif opcion == "4":
            catalogo.registrar_producto()
        elif opcion == "0":
            print("Sesión finalizada.")
            break
        else:
            print("Opción no válida.")
