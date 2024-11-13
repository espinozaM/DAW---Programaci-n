# Escribe un programa que lea una frase (entrada por teclado), y la pase como 
# parámetro a un procedimiento. El procedimiento contará el número de vocales 
# (de cada una) que aparecen en la frase, y lo imprimirá por pantalla.

def contarVocales(texto):
    vocales = 'aeiouAEIOU'
    total = 0
    for letra in texto:
        if letra in vocales:
            total += 1
    
    print(total)

frase = input('Escribe una frase: ')

contarVocales(frase)