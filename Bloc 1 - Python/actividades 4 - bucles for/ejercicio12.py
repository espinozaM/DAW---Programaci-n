'''
Escribe un programa que pida un número y escriba si primo o no
Dame un número: 123
El número 123 no es primo
Dame un número:127
El número 127 es primo
'''


numero = int(input('Dame un número: '))

'''
es_primo = True
for i in range(2, int(numero ** 0.5) + 1):
    print(numero, '/', i, '= 0')
    if numero % i == 0:
        es_primo = False
        break

if es_primo:
    print('El número %s es primo' % numero)
else:
    print('El número %s no es primo' % numero)
'''


es_primo=True
for i in range(2, int(numero/2)+1):
    if numero % i == 0:
        es_primo=False
        print(es_primo)
        break
        #print(i, end=', ')

if es_primo:
    print('Es primo')
else:
    print('No es primo')
'''
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
'''