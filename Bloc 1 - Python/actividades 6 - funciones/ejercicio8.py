# Escribe un programa que pida una frase (entrada por teclado), y pase la frase 
# como parámetro a una función que debe eliminar los espacios en blanco 
# (compactar la frase). El programa principal imprimirá por pantalla el 
# resultado final.

def eliminarEspacios(texto):
    nuevaFrase = ''
    for letra in texto:
        if letra == ' ':
            letra = ''
        nuevaFrase += letra
    
    return nuevaFrase


frase = input('Escribe una frase: ')
print(eliminarEspacios(frase))