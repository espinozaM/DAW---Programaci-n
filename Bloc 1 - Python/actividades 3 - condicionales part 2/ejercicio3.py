# Pida al usuario si quiere calcular el área de un triángulo o un cuadrado, y pida los datos
# según que caso y muestre el resultado.

opcion = input('Escribe "triangulo" o "cuadrado" para calcular el area: ')

if opcion == 'triangulo':
    base = float(input('Escribe la base: '))
    altura = float(input('Escribe la altura: '))

    area = (base * altura) / 2

    print(f"El área del triángulo es: {area}")

elif opcion == 'cuadrado':
    lado = float(input('Escribe el lado del cuadrado: '))
    area = lado * lado

    print(f"El área del cuadrado es: {area}")

