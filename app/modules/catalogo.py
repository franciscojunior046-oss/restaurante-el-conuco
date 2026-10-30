from app.database.repository import listar, insertar

def mostrar_resumen():
    print("\n--- RESUMEN DE REGISTROS ---")
    for tabla in ("clientes", "empleados", "mesas", "productos", "reservas", "pedidos"):
        print(f"{tabla.capitalize()}: {len(listar(tabla))}")

def registrar_cliente():
    nombre = input("Nombre del cliente: ").strip()
    if not nombre:
        print("El nombre es obligatorio.")
        return
    telefono = input("Teléfono: ").strip()
    correo = input("Correo: ").strip()
    insertar("clientes", {"nombre": nombre, "telefono": telefono, "correo": correo})
    print("Cliente registrado correctamente.")

def registrar_mesa():
    try:
        numero = int(input("Número de mesa: "))
        capacidad = int(input("Capacidad de personas: "))
        if numero <= 0 or capacidad <= 0:
            raise ValueError
        insertar("mesas", {"numero": numero, "capacidad": capacidad})
        print("Mesa registrada correctamente.")
    except ValueError:
        print("Introduce números enteros positivos. Verifica que el número de mesa no exista.")

def registrar_producto():
    nombre = input("Nombre del plato: ").strip()
    if not nombre:
        print("El nombre es obligatorio.")
        return
    categoria = input("Categoría: ").strip()
    try:
        precio = float(input("Precio: "))
        if precio < 0:
            raise ValueError
    except ValueError:
        print("El precio debe ser un número igual o mayor que cero.")
        return
    insertar("productos", {"nombre": nombre, "categoria": categoria, "precio": precio})
    print("Producto registrado correctamente.")
