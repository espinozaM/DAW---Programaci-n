# Escribe un programa que te pida una frase y una vocal (entrada por teclado), 
# y pase estos datos como parámetro a una función que se encargará de cambiar 
# todas las vocales de la frase por la vocal seleccionada. La función devolverá 
# la frase modificada, y el programa principal la imprimirá.

def cambiarVocal(frase, vocal):
    vocales = 'aeiouAEIOU'
    nuevaFrase = ''
    for letra in frase:
        if letra in vocales:
            letra = vocal
        nuevaFrase += letra

    return nuevaFrase


frase = input('Escribe una frase: ')
vocal = input('Escribe una vocal: ')

resultado = cambiarVocal(frase, vocal)

print(resultado)