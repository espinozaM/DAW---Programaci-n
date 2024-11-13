# Escribe un programa que pida una frase (entrada por teclado) y le pase como 
# parámetro a una función dicha frase. La función debe sustituir todos los 
# espacios en blanco de la frase por un asterisco y devolver el resultado para 
# que el programa principal la imprima por pantalla.

def espacioAsterisco(frase):
    nuevaFrase = ''
    for letra in frase:
        if letra == ' ':
            letra = '*'
        nuevaFrase += letra

    return nuevaFrase


frase = input('Escribe una frase: ')

resultado = espacioAsterisco(frase)

print(resultado)