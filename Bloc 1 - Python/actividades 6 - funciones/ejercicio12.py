# Escribir un programa que lea una frase y pase ésta como parámetro a una 
# función que debe contar el número de palabras que contiene. El programa 
# principal debe imprimir el resultado.
# A. Asumir que cada palabra está separada por un solo blanco.
# B. No se sabe cómo están separadas las palabras. Pueden estar separadas 
#    por más de un blanco o por signos de puntuación.

def contarPalabras(texto):
    total = 0
    for letra in texto:
        if letra == ' ':
            total += 1

    return total + 1


frase = input('Escribe una frase: ')

print(contarPalabras(frase))