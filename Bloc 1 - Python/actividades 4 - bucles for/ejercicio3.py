'''
Escribe un programa que pida dos números y escriba la suma de enteros desde el primero hasta el último.
Dame un número: 30
Dame otro número mayor que 30: 32
La suma desde 30 hasta a 32 es: 93
30+31+32 = 93
'''

min = int(input('Escribe un número: '))
max = int(input('Escribe un número mayor que %s: ' % min)) 

total = 0
operacion = ''

for i in range(min, max+1):
    total += i
    if i != max:
        operacion += str(i) + '+'
    else:
        operacion += str(i) + '=' + str(total)

print('La suma desde', min, 'hasta', max, 'es: ', total)
print(operacion)