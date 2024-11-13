'''
orden de precendencia
NOT
AND
OR


'hola' < 'hola'
False
'hola' <= 'hola'
True

'''
while True:
    nombre=input("Como te llamas? ")
    edad=input("Cuantos años tienes? ")
    try:
        edadFut=int(edad)+2
        print("Hola", nombre, "dentro de 2 años tendras", edadFut, "años")
        break
    #except TypeError
    except ValueError:
        print("Valor introducido incorrecto")

