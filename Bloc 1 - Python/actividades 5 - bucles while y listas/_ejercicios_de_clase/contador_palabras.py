# pedimos texto y contamos palabras

texto = input('Escribe un texto: ')

count = 0

for letra in texto:
    if letra == ' ':
        count += 1

if texto[-1] != ' ':
    count += 1

print(f'Hay {count} palabras')

