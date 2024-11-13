''''
Escribe un programa que pida dos números y escriba qué números entre ese par de números son pares y cuáles impares
Ejemplo:
Escribe un número: 4
Escribe un número mayor que 4: 8
El número 4 es par
El número 5 es impar
El número 6 es par
El número 7 es impar
El número 8 es par
'''
min = int(input('Escribe un número: '))
max = int(input('Escribe un número mayor que %s: ' % min)) 

for i in range(min, max+1):
    if i % 2 == 0:
        print('El número', i, 'es par')
    else:
        print('El número', i, 'es impar')