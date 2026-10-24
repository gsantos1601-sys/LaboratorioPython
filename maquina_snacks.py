#Maquina Snack
print('\n**** MAQUINA DE SNACKS ****')

productos = [
    {'id': 1, 'Producto': 'Papas', 'Stock': 0, 'Precio': 30.00},
    {'id': 2, 'Producto': 'Cocacola', 'Stock': 10, 'Precio': 25.00},
    {'id': 3, 'Producto': 'Agua', 'Stock': 10, 'Precio': 20.00},
    {'id': 4, 'Producto': 'Mani', 'Stock': 10, 'Precio': 10.00},
    {'id': 5, 'Producto': 'Gomitas', 'Stock': 10, 'Precio': 5.00}
]

productos_comprados = []
saldo = 0.0
total_ingresado = 0.0

def mostrar_menu():
    print('\n MENU:')
    print('''
    1. Mostrar snacks
    2. Comprar snack
    3. Mostrar Factura
    4. Salir
    ''')

#Validacion de enteros  #Pendiente aescalar para validar mas errores.
def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print('Debe ingresar un número entero.')

def mostrar_productos():
    print('\n******* SNACKS *******')
    for prod in productos:
        print(f'ID: {prod.get("id")} | Producto: {prod.get("Producto")} | '
              f'Cantidad disponible: {prod.get("Stock")} | Precio: RD$ {prod.get("Precio")}')

def buscar_producto(): #Busca por id, valida existencia y Stock.
    id_buscar = leer_entero('Introduce un ID: ')
    for producto in productos:
        if producto.get('id') == id_buscar:
            if producto["Stock"] > 0: #.Get solo lee, si es para modificar se debe usar [ corchete.
                print('Producto existe y quedan disponibles')
                return producto
            else:
                print('Producto existe pero no hay disponible')
                return buscar_producto()
    print('No existe un producto con ese ID')
    return buscar_producto()

def solicitar_dinero(saldo):
    while True:
        try:
            dinero_recibido = float(input('Ingrese el dinero para la compra: '))
            if dinero_recibido <= 0:
                print('Debe ingresar un valor mayor a 0')
            else:
                saldo += dinero_recibido
                return saldo, dinero_recibido
        except ValueError:
            print('Debe ingresar un valor numerico')

def comprar(saldo, producto):
    if saldo >= producto.get('Precio'):
        saldo -= producto.get('Precio')
        producto['Stock'] -= 1
        productos_comprados.append(producto)
        print('Compra exitosa.')
    else:
        faltante = producto.get('Precio') - saldo
        print(f'Saldo insuficiente. Te faltan RD$ {faltante:.2f}')
    return saldo

def factura(saldo, total_ingresado):
    if not productos_comprados:
        print('Aún no has comprado nada.')
        return
    print('\n******* FACTURA *******')
    total = 0
    for item in productos_comprados:
        print(f'{item.get("Producto")} ... RD$ {item.get("Precio"):.2f}')
        total += item.get('Precio')
    print(f'Total: RD$ {total:.2f}')
    print(f'Pagó con: RD$ {total_ingresado:.2f}')
    print(f'Cambio/Saldo restante: RD$ {saldo:.2f}')
    print(f'\nHistorial de compras: {productos_comprados}')

if __name__ == '__main__':

    while True:
        mostrar_menu()
        opcion = leer_entero('Seleccione una opción: ')

        if opcion == 4:
            print('Saliendo del sistema...\n')
            break
        elif opcion == 1:
            mostrar_productos()
        elif opcion == 2:
            producto = buscar_producto()
            while saldo < producto.get('Precio'):
                saldo, dinero_recibido = solicitar_dinero(saldo)
                total_ingresado += dinero_recibido
            saldo = comprar(saldo, producto)
        elif opcion == 3:
            factura(saldo, total_ingresado)
        else:
            print('Digite una opción válida.')