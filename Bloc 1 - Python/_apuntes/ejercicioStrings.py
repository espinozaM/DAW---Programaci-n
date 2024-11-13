# 9.10.2024

texto = input('Introduce un texto: ')

vocales = 'aeiou'
new = ''

'''
for vocal in vocales:
    for letra in texto:
        if vocal == letra:
            print(letra)
'''


for i in range(len(texto)):
    trobat, j = False, 0

    while not trobat and j<len(vocales):
        if texto[i] == vocales[j]:
            trobat = True
        j += 1
    if trobat:
        new += texto[i]

for letra in texto:
    j = 0
    trobat = False # reinicializa False
    while not trobat and j<len(vocales):
        if letra == vocales[j]: # se encuentra vocal
            trobat = True
        j += 1
    if trobat:
        new += letra

new = ''
for letra in texto:
    for vocal in vocales:
        if letra == vocal:
            break
        
        new += letra


for letra in texto:
    if letra not in vocales:
        new += letra


print(new)
