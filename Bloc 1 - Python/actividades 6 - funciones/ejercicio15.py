# Desarrolla un programa utilizando la metodología "pair programming"
# para gestionar contactos. La información a gestionar incluirá el 
# teléfono, nombre, primer apellido, segundo apellido y correo electrónico.
# El programa tendrá un menú con las siguientes opciones:
# - Añadir contacto
# - Consultar contacto a partir de la clave
# - Consultar todos los contactos
# - Eliminar contacto
# Se recomienda utilizar lo aprendido hasta ahora (diccionarios, 
# funciones, procedimientos, etc.).

agenda = {
    'Edwin': {
        'nombre': 'Edwin',
        'apellido1': 'Espinoza',
        'apellido2': 'Mercado',
        'telefono': 612345678,
        'email': 'eespinoza@gmail.com'
    }
}

# FUNCIONES

def añadirContacto(nombre, apellido1, apellido2, telefono, email):
    contacto = {
        'nombre': nombre,
        'apellido1': apellido1,
        'apellido2': apellido2,
        'telefono': telefono,
        'email': email
    }

    agenda[nombre] = contacto


def mostrarContacto(nombre):
    # en caso que no existe contacto
    if agenda.get(nombre, None) is None:
        print('No existe el contacto', nombre)
        return
    
    # imprime detalles de contacto
    for propiedad, valor in agenda[nombre].items():
        print(f'{propiedad.capitalize()}: {valor}')


def mostrarTodosContactos():
    print('-' * 44)
    for contacto in agenda:
        print('Contacto:', agenda[contacto]['nombre'], '\n')

        for propiedad, valor in agenda[contacto].items():
            print(f'{propiedad.capitalize()}: {valor}')
    print('-' * 44)


def eliminarContacto(nombre):
    # comprobar que contacto existe
    if agenda.get(nombre, None) is None:
        print('No se ha eliminado ningun contacto.')
        return
    agenda.pop(nombre)
    print('Se ha eliminado:', nombre)


userInput = ''
while userInput != '5':
    print('''
1 - Añadir contacto
2 - Consultar contacto a partir de la clave
3 - Consultar todos los contactos
4 - Eliminar contacto
5 - Salir
          ''')
    userInput = input('Elige una opción: ')
    if userInput == '1':
        print('Información del contacto:')
        nombre = input('Nombre: ')
        apellido1 = input('Primer apellido: ')
        apellido2 = input('Segundo apellido: ')
        telefono = input('Telefono: ')
        email = input('Correo electrónico: ')

        añadirContacto(nombre, apellido1, apellido2, telefono, email)

    elif userInput == '2':
        nombre = input('Escribe el nombre del contacto a consultar: ')
        mostrarContacto(nombre)
    
    elif userInput == '3':
        mostrarTodosContactos()
    
    elif userInput == '4':
        nombre = input('Escribe el nombre del contacto a eliminar: ')
        eliminarContacto(nombre)


