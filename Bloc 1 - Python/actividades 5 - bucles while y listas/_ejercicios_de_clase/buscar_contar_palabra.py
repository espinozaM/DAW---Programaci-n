# pedimos texto y una palabra
# contamos las veces que aparece esa palabra

texto = input('Escribe un texto: ')
palabra = input('Escribe una palabra: ')

count = 0
temp_palabra = ''



i=0
while i < len(texto):
    # saltar los espacios en blanco
    while i < len(texto) and texto[i] == ' ':
        i+=1
    
    j=0
    encaja = True

    # comprobar si la palabra coincide
    while i < len(texto) and j < len(palabra) and encaja:
        if texto[i] == palabra[j]:
            i+=1
            j+=1
        else:
            encaja = False

    # Verificar si hemos encontrado la palabra completa
    if j == len(palabra) and (i == len(texto) or texto[i] == ' '):
        count += 1

    # Avanzar hasta el próximo espacio o palabra
    while i < len(texto) and texto[i] != ' ':
        i += 1

# Mostrar el número de veces que aparece la palabra
print(f"La palabra '{palabra}' aparece {count} veces en el texto.")