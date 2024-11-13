# Programa que lee una frase ingresada por teclado y la pasa como parámetro
# a un procedimiento. Este procedimiento muestra cada carácter de la frase
# en cada línea.

def muestraLetras(frase):
    for letra in frase:
        print(letra)


frase = input('Escribe una frase: ')

muestraLetras(frase)