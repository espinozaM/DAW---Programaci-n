'''
Escribe un programa que pida notas y los guarde en una lista. Para terminar de introducir notas, 
escribe una nota que no esté entre 0 y 10. El programa termina escribiendo la lista de notas.
Escribe una nota: 7.5
Escribe una nota: 0
Escribe una nota: 10
Escribe una nota: -1
Las notas que has Escrito son [7.5, 0.0, 10.0]
'''

parar = False
lista_numeros = []

while parar == False:
    numero = float(input('Escribe un número: '))
    
    if 0 <= numero <= 10:
        # añade nota entre 0 y 10 en la lista
        lista_numeros.append(numero)
    else:
        # salir del programa
        parar = True


print('Las notas que has escrito son: ', lista_numeros)