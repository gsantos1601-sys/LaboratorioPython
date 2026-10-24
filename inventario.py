#seg 10 cap 175

inventarios = [
    {'id': 1, 'Producto': 'Leche', 'Stock': 10, 'Precio': 50.99},
    {'id': 2, 'Producto': 'Pan', 'Stock': 5, 'Precio': 9.99},
    {'id': 3, 'Producto': 'Mantequilla', 'Stock': 3, 'Precio': 5.99}
]


def mostrar_menu():
    print('\n**** INVENTARIO DE PRODUCTOS ****')
    print('''
    1. Mostrar inventario
    2. Agregar nuevo producto
    3. Buscar producto por ID
    4. Salir
    ''')


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print('Debe ingresar un número entero.')


def leer_decimal(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print('Debe ingresar un número válido.')


def volver_al_menu():
    while True:
        respuesta = input('\nDesea volver al menu de opciones? Si/No: ').lower().strip()
        if respuesta in ('si', 'sí'):
            return True
        if respuesta == 'no':
            return False
        print('Responda únicamente Si o No.')


def siguiente_id():
    return max((p['id'] for p in inventarios), default=0) + 1


def imprimir_producto(p):
    print(f'ID: {p["id"]} | Producto: {p["Producto"]} | '
          f'Cantidad disponible: {p["Stock"]} | Precio: RD$ {p["Precio"]}')


def mostrar_inventario():
    print('\n**** INVENTARIO ****')
    for producto in inventarios:
        imprimir_producto(producto)


def agregar_producto():
    print('\n*** AGREGAR PRODUCTO ***')
    nombre = input('Ingrese el producto: ').strip().capitalize()
    cantidad = leer_entero('Ingrese la cantidad disponible: ')
    precio = leer_decimal('Ingrese el precio: ')

    if cantidad < 0 or precio < 0:
        print('La cantidad y el precio no pueden ser negativos.')
        return

    inventarios.append({
        'id': siguiente_id(),
        'Producto': nombre,
        'Stock': cantidad,
        'Precio': precio
    })
    print('Producto agregado correctamente.')


def buscar_producto():
    id_buscar = leer_entero('Introduce un ID: ')
    for producto in inventarios:
        if producto['id'] == id_buscar:
            imprimir_producto(producto)
            return
    print('Ese ID no existe.')


while True:
    mostrar_menu()
    opcion = leer_entero('Seleccione una opción: ')

    if opcion == 4:
        print('Saliendo del sistema...\n')
        break
    elif opcion == 1:
        mostrar_inventario()
    elif opcion == 2:
        agregar_producto()
    elif opcion == 3:
        buscar_producto()
    else:
        print('Digite una opción válida.')
        continue

    if not volver_al_menu():
        print('El sistema fue finalizado correctamente.')
        break