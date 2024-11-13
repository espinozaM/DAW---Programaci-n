'''
Escribe un programa que pida la anchura de un triángulo y lo dibuje de la siguiente manera:
Altura del triángulo: 4
*
**
***
****
***
**
*

'''

altura = int(input('Altura del triangulo: '))

for i in range(1, altura+1):
    print('*' * i)
for i in range(altura-1, 0, -1):
    print('*' * i)