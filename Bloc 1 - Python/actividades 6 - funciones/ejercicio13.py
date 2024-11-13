# Escribe un programa que le pida al usuario si quiere calcular si un número 
# es primo usando un bucle "for" o "while". 
# Habrá dos funciones que realizan 
# el mismo cálculo, una usando "for" (sin "breaks") y otra usando "while". 
# Ambas funciones devolverán True si el número es primo, o False si no lo es.
# El programa principal mostrará el resultado.
# Como mejora, puedes calcular el tiempo que tarda en encontrar la solución 
# con cada método. 
# Comentario: aprovecha el código que tienes ya creado.

import time

def es_primo_for(numero):
    
    es_primo = True

    if numero < 2:
        es_primo = False
    
    for i in range(2, int(numero/2)+1):
        if numero % i == 0:
            es_primo = False

    return es_primo


def es_primo_while(numero):
    
    es_primo = True
    
    if numero < 2:
        es_primo = False
    
    i = 2
    while es_primo and i <= int(numero/2):
        if numero % i == 0:
            es_primo = False
        i += 1

    return es_primo

numero = 104729

inicio = time.time()
resultado_for = es_primo_for(numero)
tiempo = time.time() - inicio
print(f"Resultado usando 'for' es: {resultado_for}. Tiempo de ejecución: {tiempo:.6f} segundos")

inicio = time.time()
resultado_while = es_primo_while(numero)
tiempo = time.time() - inicio
print(f"Resultado usando 'while' es: {resultado_while}. Tiempo de ejecución: {tiempo:.6f} segundos")

