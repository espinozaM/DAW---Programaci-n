'''
pedimos un texto y un contador,
contamos cuantas veces aparece dicho caracter en el texto
'''

texto = input('Escribe un texto: ')
caracter = input('Escribe un caracter: ')
count = 0

for letra in texto:
    if letra == caracter:
        count += 1

print(f'La letra {caracter} aparece {count} veces')