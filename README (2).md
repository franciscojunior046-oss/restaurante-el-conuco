# Sistema de Gestión del Restaurante El Conuco

Proyecto base organizado para la actividad **Proyecto Base** de Desarrollo de Aplicaciones y Sistemas Informáticos.

## Objetivo
Organizar en una aplicación la información de usuarios, empleados, clientes, mesas, menú, reservas, pedidos, facturación, pagos e inventario del Restaurante El Conuco.

## Tecnologías de esta versión inicial
- Python 3.10 o superior.
- SQLite para que el proyecto pueda ejecutarse localmente sin instalar un servidor.
- Tkinter/terminal: esta entrega contiene una aplicación inicial por consola.
- Git y GitHub para el control de versiones.

> Nota: el documento de análisis propone Python y una base de datos relacional, pero no especifica el motor. Por eso esta estructura usa SQLite como base local de desarrollo. Si el profesor exige SQL Server, habrá que adaptar `app/database/connection.py` y las consultas.

## Estructura
```text
sistema_gestion_el_conuco/
├── main.py
├── requirements.txt
├── .gitignore
├── .env.example
├── app/
│   ├── config/
│   ├── database/
│   ├── modules/
│   │   ├── login/
│   │   ├── usuarios/
│   │   ├── empleados/
│   │   ├── clientes/
│   │   ├── mesas/
│   │   ├── menu/
│   │   ├── reservas/
│   │   ├── pedidos/
│   │   ├── facturacion/
│   │   ├── inventario/
│   │   └── reportes/
│   └── utils/
├── docs/
├── tests/
└── data/
```

## Ejecutar
1. Instala Python 3.10 o superior.
2. Abre esta carpeta en Visual Studio Code.
3. Abre la terminal y ejecuta `python main.py`.
4. La base de datos `data/el_conuco.db` y sus tablas se crean automáticamente la primera vez.

## Usuario inicial
Al iniciar por primera vez se crea:
- Usuario: `admin`
- Contraseña: `admin123`

Cambia esa contraseña después de iniciar el sistema. Las contraseñas se guardan usando hash, no como texto plano.

## Publicar en GitHub
Crea un repositorio vacío en GitHub y ejecuta desde la terminal de esta carpeta:
```bash
git init
git add .
git commit -m "Proyecto base Sistema El Conuco"
git branch -M main
git remote add origin https://github.com/TU-USUARIO/TU-REPOSITORIO.git
git push -u origin main
```
Sustituye la URL de ejemplo por la URL real de tu repositorio.

## Estado del proyecto
La estructura, configuración, conexión local, creación inicial de tablas, autenticación y menú de navegación están implementados. Los módulos de gestión tienen funciones iniciales de consulta/registro y pueden ampliarse con pantallas, validaciones y permisos completos.
