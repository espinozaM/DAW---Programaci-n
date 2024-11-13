# Programa que lee el nombre y dos apellidos de una persona como
# tres cadenas de caracteres. Los pasa a una función que los une
# y devuelve una única cadena, que luego se imprime en pantalla.

def unirNombre(nombre, apellido1, apellido2):
    return f'{nombre} {apellido1} {apellido2}'


n = input('Escribe tu nombre: ')
a1 = input('Escribe tu apellido: ')
a2 = input('Escribe tu segundo apellido: ')

print(unirNombre(n,a1,a2))