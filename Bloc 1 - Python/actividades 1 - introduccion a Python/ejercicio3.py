# ejercicio 3
# número es par o impar

n = int(input('Introduce un número: '))

#if n == 0:
#    print('Es cero') # redundante, cero es par
if n % 2 == 0:
    print('Es par')
else:
    print('Es inpar')
print('Adios')