# Escribe un programa que lea el nombre de una persona y un carácter 
# (entrada por teclado), y le pase estos datos a una función que comprobará 
# si dicho carácter está en su nombre. El resultado de dicha función lo 
# imprimirá el programa principal por pantalla.


def existeCaracter(texto, caracter):
    return caracter in texto

nombre = input('Escribe tu nombre: ')
caracter = input('Escribe un caracter: ')

resultado = existeCaracter(nombre, caracter)

print(resultado)

