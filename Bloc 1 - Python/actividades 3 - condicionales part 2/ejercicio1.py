
'''
Realiza un programa que:
Pida al usuario 5 números y diga cuál es el mayor y cuál el menor.
 	
Pida al usuario 5 números y diga si estos estaban en orden decreciente, 	creciente o desordenados.
 	
Pida al usuario si quiere calcular el área de un triángulo o un cuadrado, y pida los datos según que caso y muestre el resultado.
 	
Pida al usuario tres números y un cuarto número, y compruebe si este último es divisor de los tres números primeros.
 	
Pida al usuario un importe en euros y diga si el cajero automático le 	puede dar dicho importe utilizando el mismo billete y el más grande 	(recuerda que el billete puede ser de 500, 200, 100, 50, 20, 10 y 5 	€).
 	
Por ejemplo: 
25 euros → “el cajero te devuelve 5 billetes de 5 euros”
 	
20 euros → “el cajero te devuelve 1 billete de 20 euros”
 	
130 euros → “el cajero te devuelve 13 billetes de 10 euros”
'''

n1 = int(input('Introduce un número: '))
n2 = int(input('Introduce otro número: '))
n3 = int(input('Introduce otro número: '))
n4 = int(input('Introduce otro número: '))
n5 = int(input('Introduce otro número: '))

mayor = n1
menor = n1

if n2 > mayor:
    mayor = n2
if n3 > mayor:
    mayor = n3
if n4 > mayor:
    mayor = n4
if n5 > mayor:
    mayor = n5

print('El número mayor es', mayor)

if n2 < mayor:
    menor = n2
if n3 < mayor:
    menor = n3
if n4 < mayor:
    menor = n4
if n5 < mayor:
    menor = n5

print('El número menor es', menor)
