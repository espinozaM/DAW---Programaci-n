# Escribe un programa que te pida una frase y pase la frase como parámetro a 
# una función. La función debe devolver si la frase es palíndroma o no, y el 
# programa principal escribirá el resultado por pantalla.

def esPalindromo(texto):
    # eliminar espacios en blanco
    nuevoTexto = ''
    for letra in texto:
        if letra == ' ':
            letra =''
        nuevoTexto += letra

    return nuevoTexto == nuevoTexto[::-1]


frase = input('Escribe una frase: ')

resultado = f'{frase} es palindromo.' if esPalindromo(frase) else f'{frase} no es palindromo'

print(resultado)

# salta lenin el atlas
# dabale arroz a la zorra el abad