'''
Escribe un programa que pida un número (límite) y luego te pida números hasta que la suma de los
números introducidos supere el límite inicial. El programa termina escribiendo la lista de números.
Escribe límite: 50
Escribe un valor: 10
Escribe otro valor: 25
Escribe otro valor: 7
Escribe otro valor: 14
El límite a superar es 50. La lista creada es 10, 25, 7, 14 ya que la suma de estos números es: 56
'''

limite = int(input('Escribe límite: '))

num = int(input('Escribe un valor: '))

lista_numeros = []
total = num

while total <= limite:
    lista_numeros.append(num)

    total += num
    num = int(input('Escribe otro valor: '))

    

print(f'El límite a superar es {limite}. La lista creada es', str(lista_numeros)[1:-1], 'ya que la suma de estos números es:', total)