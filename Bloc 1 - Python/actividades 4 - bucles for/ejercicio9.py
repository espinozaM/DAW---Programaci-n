'''
Escribe un programa que pida la anchura y la altura de un rectángulo y lo dibuje de la siguiente manera:
Anchura del rectángulo: 5
Altura del rectángulo: 4
*****
*   *
*   *
*****

'''

altura = int(input('Altura del rectángulo: '))
anchura = int(input('Anchura del rectángulo: '))

for i in range(altura):
    fila = ''
    for x in range(anchura):
        if i == 0 or i == altura-1: # primer o ultima linea
            fila += '*'
        elif x == 0 or x == anchura-1: # primer o ultima columna
            fila += '*'
        else:
            fila += ' ' # imprime blanco en las columnas del medio
    print(fila)

# pintamos primera línea
for i in range(anchura):
    print('*', end='')
print('')

# pintamos líneas del medio
for i in range(altura-2):
    print('*', end='')
    for j in range(anchura-2):
        print(' ', end='')
    print('*', end='')
    print('')

# pintamos la última línea
for i in range(anchura):
    print('*', end='')
print('')