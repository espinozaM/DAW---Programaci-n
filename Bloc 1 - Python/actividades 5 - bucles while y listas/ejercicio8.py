'''
Escribe un programa que te pida primero un número y luego te pida números hasta que la suma de los números
introducidos coincida con el número inicial. El programa termina escribiendo la lista de números.
Escribe límite: 50
Escribe un valor: 10
Escribe otro valor: 45
45 es demasiado grande. Escribe otro valor: 1
Escribe otro valor: 39
El límite a alcanzar es 50. La lista creada es: 10, 1, 39
'''

limite = int(input('Escribe límite: '))

total = int(input('Escribe un valor: '))

lista_numeros = [total]

while total != limite:
    numActual = int(input('Escribe otro valor: '))

    while (numActual + total) > limite:
        numActual = int(input(f'{numActual} es demasiado grande. Escribe otro valor: '))
    
    lista_numeros.append(numActual)
    total += numActual

print(f'El límite a alcanzar es {limite}. La lista creada es:', str(lista_numeros)[1:-1])


