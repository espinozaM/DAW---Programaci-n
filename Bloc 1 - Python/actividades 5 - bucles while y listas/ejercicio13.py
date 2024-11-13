'''
Desarrolla de nuevo el ejercicio de la práctica anterior de los números primos, con while.
Reflexiona y escribe en el propio programa en forma de comentario, qué opción es mejor y por qué.
'''

numero = int(input('Dame un número: '))

es_primo = True

i = 2
while es_primo and i <= int(numero/2):
    if numero % i == 0:
        es_primo = False
    i += 1

if es_primo:
    print('Es primo')
else:
    print('No es primo')