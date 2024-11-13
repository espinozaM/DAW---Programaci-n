

# Pida al usuario 5 números y diga si estos estaban en orden decreciente, 	creciente o desordenados.
n1 = int(input('Introduce un número: '))
n2 = int(input('Introduce otro número: '))
n3 = int(input('Introduce otro número: '))
n4 = int(input('Introduce otro número: '))
n5 = int(input('Introduce otro número: '))

anterior = n1
menor = n1

if n2 > anterior:
    anterior = n2
elif n3 > anterior:
    anterior = n3
elif n4 > anterior:
    anterior = n4
elif n5 > anterior:
    anterior = n5
    print('orden creciente')
else:
    print('Orden decreciente')
