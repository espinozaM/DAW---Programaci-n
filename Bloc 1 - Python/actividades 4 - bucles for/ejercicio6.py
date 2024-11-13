'''
Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:
Altura del triángulo: 4
*
**
***
****
'''

altura = int(input('Altura del triangulo: '))

#for i in range(1, altura+1):
#    print('*' * i)

for i in range(altura):
    for j in range(i+1):
        print('*', end='')
    print('\n')