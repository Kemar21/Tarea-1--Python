#Funcion para suamr
def sumar(a, b):
    c = a + b
    return 'El resultado de la suma ' + str(a) + ' + ' + str(b) + ' es: ' + str(c)

#Funcion para restar
def restar(a, b):
    c = a - b
    return 'El resultado de la resta ' + str(a) + ' - ' + str(b) + ' es: ' + str(c)

#Funcion para multiplicar
def multiplicar(a, b):
    c = a * b
    return 'El resultado de la multiplicacion ' + str(a) + ' * ' + str(b) + ' es: ' + str(c)

#Funcion para dividir
def dividir(a, b):
    c = a / b
    return 'El resultado de la division ' + str(a) + ' / ' + str(b) + ' es: ' + str(c)

#Menu
def menu():
    print('Bienvenido')
    print('Calculadora Basica')
    print('Menu:\n',
          '1- Sumar\n',
          '2- Restar\n',
          '3- Multiplicar\n',
          '4- Dividir\n',
          '5- Salir\n')
    opcion = int(input("Ingrese una opcion a procesar?\n"))

    if(opcion <= 5):
        if opcion == 1:
            try:
                a = int(input("Ingrese el primer numero\n"))
                b = int(input('Ingrese el segundo numero\n'))
                print(sumar(a, b))
            except:
                print('Ha ocurrido un error')
            finally:
                menu()
        elif opcion == 2:
             try:
                 a = int(input("Ingrese el primer numero\n"))
                 b = int(input('Ingrese el segundo numero\n'))
                 print(restar(a, b))
             except:
                print('Ha ocurrido un error')

             finally:
                 menu()
        elif opcion == 3:
            try:
                a = int(input("Ingrese el primer numero\n"))
                b = int(input('Ingrese el segundo numero\n'))
                print(multiplicar(a, b))
            except:
                print('Ha ocurrido un error')
            finally:
                menu()
        elif opcion == 4:
             try:
                 a = int(input("Ingrese el primer numero\n"))
                 b = int(input('Ingrese el segundo numero\n'))
                 print(dividir(a, b))
             except:
                 print('Ha ocurrido un error')
             finally:
                 menu()
        elif opcion == 5:
            print('Fin de la calculadora')
            exit()
    else:
        print('Opcion invalida')
        menu()

print(menu())
