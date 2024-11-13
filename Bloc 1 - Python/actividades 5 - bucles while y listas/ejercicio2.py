'''
Escribe un programa que te pida números y los guarde en una lista. 
Para terminar de introducir número, simplemente escribe “Salir”. El programa termina escribiendo la lista de números.
Escribe un nombre: 14
Escribe una otro nombre: 123
Escribe una otro nombre: -25
Escribe una otro nombre: 123
Escribe una otro nombre: Salir
Los números que has escrito son [14, 123, -25, 123]

'''

parar = False
lista_numeros = []

while parar == False:
    numero = input('Escribe un número: ')

    #if numero == '': continue # usuario pulsa enter ''
    
    if numero.lower() == 'salir' or numero == '': # 
        parar = True
    else:
        #ValueError: invalid literal for int() with base 10: '1.2'
        # enteros y decimales
        lista_numeros.append(int(numero))

print('Los números que has escrito son: ', lista_numeros)