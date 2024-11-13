# Escribe un programa que te pida una palabra o número, y pase estos datos 
# como parámetro a una función. La función debe determinar si el valor es 
# palíndromo o capicúa. El programa principal imprimirá el resultado de la función.

def esPalindromo(texto):
    return texto == texto[::-1]


texto = input('Escribe una palabra o un texto: ')

resultado = f'{texto} es palindromo.' if esPalindromo(texto) else f'{texto} no es palindromo.'

print(resultado)