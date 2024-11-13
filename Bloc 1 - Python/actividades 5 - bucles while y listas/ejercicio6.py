'''
Escribe un programa que pida primero dos números (máximo y mínimo) y que después te pida números intermedios.
Para terminar de escribir números, escribe un número que no esté comprendido entre los dos valores iniciales.
El programa termina escribiendo la lista de números.
Escribe un número: 6
Escribe un número mayor que 6: 4
4 no es mayor que 6. Vuelve a probar: 50
Escribe un número entre 6 y 50: 45
Escribe otro número entre 6 y 50: 13
Escribe otro número entre 6 y 50: 4
Los números situados entre 6 y 50 que has escrito son: 45, 13 
'''

min = int(input('Escribe un número: '))
max = int(input(f'Escribe un número mayor que {min}: '))

while max <= min:
    max = int(input(f'{max} no es mayor que {min}. Vuelve a probar: '))

num = int(input(f'Escribe un número entre {min} y {max}: '))
lista_numeros = []

while min < num < max:
    lista_numeros.append(num)
    num = int(input(f'Escribe otro número entre {min} y {max}: '))

print(f'Los números situados entre {min} y {max} que has escrito son:', str(lista_numeros)[1:-1])