# Pide al usuario un importe en euros y verifica si el cajero automático
# puede dar dicho importe utilizando billetes del mismo valor y el más grande.
# Los billetes disponibles son de 500, 200, 100, 50, 20, 10 y 5 euros.

# Ejemplos:
# 25 euros → "el cajero te devuelve 5 billetes de 5 euros"
# 20 euros → "el cajero te devuelve 1 billete de 20 euros"
# 130 euros → "el cajero te devuelve 13 billetes de 10 euros"

importe = float(input('Introduce un valor: '))

if importe % 500:
    billete_cambio = 500
elif importe % 200:
    billete_cambio = 200
elif importe % 100:
    billete_cambio = 100
elif importe % 50:
    billete_cambio = 50
elif importe % 20:
    billete_cambio = 20
elif importe % 10:
    billete_cambio = 10
elif importe % 5:
    billete_cambio = 5
else:
    billete_cambio = None

if billete_cambio:
    cantidad_billetes = importe // billete_cambio
    print(f"el cajero te devuelve {cantidad_billetes} billetes de {billete_cambio} euros")
else:
    print('No devuelve cambio')


