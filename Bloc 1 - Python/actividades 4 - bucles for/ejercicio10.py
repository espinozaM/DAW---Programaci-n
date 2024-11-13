'''
Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:
Altura de un triángulo: 5
    *
   ***
  *****
 *******
*********
'''

altura = int(input('Escribe la altura: '))
'''
for i in range(1, altura+1):
    espacios = ' ' * (altura - i)
    estrellas = '*' * (2 * i - 1)
    print(espacios + estrellas)
'''

for i in range(1, altura+1):
    for j in range(altura-i):
        print(' ', end='')
    #print('*' * (i*2-1))
    for j in range(1+(i-1)*2):
        print('*', end='')
    print('')

'''
# Solicitar la altura del triángulo
altura = int(input("Altura de un triángulo: "))

# Dibujar el triángulo
for i in range(1, altura + 1):
    espacios = ' ' * (altura - i)
    estrellas = '*' * (2 * i - 1)
    print(espacios + estrellas)
'''