'''
Escribe un programa que te pida dos números, de manera que el segundo sea mayor que el primero.
El programa termina escribiendo los dos números tal y como se pide:
Escribe un número: 6
Escribe un número mayor que 6: 6
6 no es mayor que 6. Vuelve a introducir un número: 1
1 no es mayor que 6. Vuelve a introducir un número: 8
Los números que has escrito son 6 y 8
'''

n1 = int(input('Escribe un número: '))
n2 = int(input(f'Escribe un número mayor que {n1}: '))


while n2 <= n1:
    n2 = int(input(f'{n1} no es mayor que {n2}. Vuelve a introducir un número: '))


print(f'Los números que has escrito son {n1} y {n2}')
