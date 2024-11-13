'''
Escribe un programa que pida un número y calcule su factorial.
Dame un número: 5
El factorial de 5 es: 120

'''

n = int(input('Dame un número: '))

resultado = 1
for i in range(1, n+1):
    resultado *= i

print('El factorial de', n, 'es:', resultado)
