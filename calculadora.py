import operaciones

#Programa principal.

if __name__ == '__main__':
  salir = False

  print('''   ***MENU****
    
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir
    5. Salir
    ''')


  while not salir:

    opciones = int(input('Seleccione una operacion a realizar: '))

    a = int(input('Ingrese un primer numero: '))
    b = int(input('Ingrese un segundo numero: '))

    if opciones == 1:
      resultado = operaciones.suma(a, b)
      print(f'La suma de los numeros es: {resultado}\n')
    elif opciones == 2:
      resultado = operaciones.resta(a, b)
      print(f'La resta de los numeros es:{resultado}\n')
    elif opciones == 3:
      resultado = operaciones.multiplicacion(a, b)
      print(f'La multiplicacion de los numeros es:{resultado}\n')
    elif opciones == 4:
      resultado = operaciones.division(a, b)
      print(f'La division de los numeros es:{resultado}\n')
    elif opciones == 5:
      print('Saliendo del sistema\n')
      salir = True
    else:
      print('Digite una opcion valida.\n')

  else:
    print('El sistema fue finalizado correctamente.')

