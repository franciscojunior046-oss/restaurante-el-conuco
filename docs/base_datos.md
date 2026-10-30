# Diseño inicial de la base de datos

La base local SQLite crea tablas para usuarios, empleados, clientes, mesas, productos, reservas, pedidos, detalle de pedido, facturas, pagos e inventario.

Las relaciones principales siguen el análisis:
- Un cliente puede tener varias reservas.
- Una mesa puede aparecer en varias reservas y pedidos.
- Un pedido puede contener varios productos mediante `detalle_pedido`.
- Una factura se relaciona con un pedido.
- Una factura puede tener uno o varios pagos.

La estructura es inicial y puede ajustarse al diagrama entidad-relación definitivo del proyecto.
