'''
Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:
Altura del triángulo: 4
****
***
**
*
'''

altura = int(input('Altura del triangulo: '))

#for i in range(altura, 0, -1):
#    print('*' * i)

for i in range(altura):
    for j in range(altura - i):
        print('*', end='')
    print('\n')