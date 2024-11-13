# ejercicio 4
# calcular el mayor de los números

a = int(input('introduce el primer número '))
b = int(input('introduce el segundo número '))

if a == b:
    print('A y B son iguales')
elif a > b:
    print('A es mayor')
else:
    print('B es mayor')

print('A es mayor' if a > b else 'B es menor')