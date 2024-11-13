'''
Escribe un programa que te pida palabras y las guarde en una lista. Para terminar de introducir palabras, simplemente pulsa Enter.
El programa termina escribiendo la lista de palabras.
Escribe una palabra: viaje
Escribe más palabras: aventura
Escribe más palabras: cómic
Escribe más palabras:
Las palabras que has Escrito son [ 'viaje', 'aventura', 'cómic']

'''
"""
parar = False
lista_palabras = []

while parar == False:
    palabra = input('Escribe una palabra: ')

    # si usuario no introduce nada "" o un espacio en blanco o pulsa Enter
    if palabra == '' or palabra == ' ':
        parar = True
    # usuario introduce palabras
    else:
        #lista_palabras.append(palabra)
        lista_palabras = lista_palabras + [palabra]

print('Las palabras que has Escrito son: ', lista_palabras)
"""

# inicializar variable palabras
palabras = []

# solicitar palabras al usuario
palabra = input('Escribe una palabras: ')

while palabra != '':
    # añadir palabra a la lista
    palabras.append(palabra)
    # pedir otra palabra a la lista
    palabra = input('Escribe más palabras: ')