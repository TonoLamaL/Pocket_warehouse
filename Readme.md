PROYECTO POCKET WAREHOUSE de EBOX

Aplicación web de administración de inventarios en tu casa

Cuenta con un entorno virtual - venv -

Pocket Warehouse

Pocket Warehouse es una aplicación web para la gestión de inventario y ventas en línea. La aplicación está diseñada para pequeñas empresas que necesitan un sistema sencillo y fácil de usar para administrar su inventario y ventas en línea.

Imagina que quieres levantar un negocio orientado a venta de productos al por menor y al por mayor.
Sabes lo que quieres vender. Vas a comprar e importar mercaderia y usar proveedores nacionales para obtener
todos los productos que tienes en mente. Como estas iniciando , no tienes otro lugar mas que tu casa para usar como bodega.

Esta herramienta te permitirá hacer un control de inventario necesario para un crecimiento sostenible.
Aqui podras tener claridad de los productos y unidades que tienes para vender. Registro se compras y ventas.
El stock (inventario disponible) es el resultado entre lo que compras y lo que vendes. El delta que queda es lo que aun tienes como activo.

El sistema permite a los usuarios revisar el estado del inventario, incluyendo las unidades disponibles, las unidades reservadas, las unidades preparadas, y las unidades entregadas en el panel "stock en linea". Los usuarios también pueden revisar las salidas para cada producto, ver las salidas pendientes, y actualizar el estado de las salidas.

Además contarás con un catálogo o maestra de productos ordenada que te permitirá abrir nuevos canales de venta, facilitar la comunicacion e identificacion de tus productos, y mucho más.

FUNCIONES

Las principales funciones de Pocket Warehouse estan en el panel de control. Estás son:

Registro y autenticación de usuarios.
Gestión de catálogo de productos (agregar, modificar y eliminar productos).
Gestión de compras
Gestión de ventas (procesar órdenes de ventas, actualizar el estado de las órdenes).
Actualización en línea del inventario en tiempo real (cuando se procesan las órdenes de compra en "ver ventas").
Visualización del stock en línea.

¿Cómo partir con pocket warehouse?

0.- Crea un usuario

1.- Debes crear tu maestra de productos 
    a.- Nombre
    b.- Sku (numero que identifica al producto)
    c.- Categoria 

2.- Registra las compras a nivel de unidades para ir sumando a tu inventario
    a.- Anota el contenedor que trae la mercaderia o el nombre sel proveedor
    b.- Busca el sku que recibiste (previamente debe eatar creado en tu maeatra)
    c.- Anota cuantas unidades son

3.- Registra tu ventas a nivel de unidades para ir restando a tu inventario 
    a.- Anota el número con el que se identifica la compra (orden de compra)
    b.- Busca el sku vendido
    c.- Anota la cantidad de unidades vendidas en esa orden

4.- Revisa tus ventas en "Ver ventas" y cambia el estado de la orden para ir ordenando tus salidas y tu inventario. A medida que vas usando lso estados podrás visualizar el stock en linea correctamente

5.- Revisa tu stock(inventario) para tener claridad de lo que te queda por vender, que debes comprar y muchas cosas mas.

ESTADOS

Las órdenes de compra en Pocket Warehouse tienen cuatro estados:

1.- Pendiente
2.- Preparado
3.- Entregado
4.- Cancelado

Para cambiar el estado de una orden de compra, se debe seguir el siguiente proceso:

        - Ir a la sección "Ver ventas".
        - Seleccionar la orden de compra que se desea actualizar.
        - Hacer clic en el botón "Cambiar".
        - Seleccionar el nuevo estado de la orden de compra en el menú desplegable.
        - Hacer clic en el botón "Actualiar".
        * Cuando se actualiza el estado de una orden de compra, el inventario se actualizará automáticamente. Por ejemplo, si una orden de compra pasa de "pendiente" a "preparado", las unidades de productos correspondientes pasarán de estar "disponibles" a "reservadas".

Una vez que hayas seleccionado el nuevo estado, el sistema verificará que el cambio sea válido, por ejemplo, si estás intentando cambiar una orden de salida de "Cancelado" a "Preparado", se mostrará un mensaje de error indicando que el cambio no es válido. Si el cambio de estado es válido, se actualizará el estado de la orden de salida y se reflejará en el inventario de la empresa.

El sistema tiene en cuenta los cambios en el inventario cuando se cambia el estado de una orden de salida. Por ejemplo, si una orden de salida cambia de "Pendiente" a "Preparado", el sistema restará las unidades correspondientes del inventario disponible y las agregará al inventario reservado. De manera similar, si una orden de salida cambia de "Preparado" a "Entregado", el sistema restará las unidades correspondientes del inventario reservado y las agregará al inventario entregado descontando las unidades disponibles que tienes pare vender o preparar nuevos pedidos.

En resumen, el cambio de estado es una función importante en Pocket Warehouse que te permite mantener un control preciso del inventario de tu empresa y asegurarte de que las órdenes de salida se manejen de manera efectiva y eficiente.

 
Tecnologías utilizadas

La aplicación fue desarrollada utilizando las siguientes tecnologías:

Python 
Django
HTML5
CSS
Bootstrap 4
SQLite3

