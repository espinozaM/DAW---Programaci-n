# pedimos texto y una palabra
# contamos las veces que aparece esa palabra

texto = input('Escribe un texto: ')
palabra = input('Escribe una palabra: ')

count = 0
palabra_temp = ''

for letra in texto:
    if letra != ' ':
        palabra_temp += letra
        
    else:
        # palabra coincide
        if palabra_temp == palabra:
            count += 1
        
        # resetea palabra temporal
        palabra_temp = ''
                
# comprobar la última palabra si no está seguida de un espacio
if palabra_temp == palabra:
    count += 1

# Mostrar el número de veces que aparece la palabra
print(f"La palabra '{palabra}' aparece {count} veces en el texto.")