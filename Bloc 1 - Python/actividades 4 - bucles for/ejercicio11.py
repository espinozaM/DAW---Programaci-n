'''
Escribe un programa que pida un número e imprima todos sus divisores.
Dame un número: 200
Los divisores de 200 son: 1 2 4 5 8 10 20 25 40 50 100 200
'''

numero = int(input('Dame un número: '))

'''
contador = 1
while contador <= numero:
    if numero % contador == 0:
        print(contador)
    contador += 1
'''

print('Los divisores son: 1, ', end='')
for i in range(2, int(numero/2)+1):
    if numero % i == 0:
        print(i, end=', ')
print(numero)
