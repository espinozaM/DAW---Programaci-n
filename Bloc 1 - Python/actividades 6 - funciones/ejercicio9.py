# Escribe un programa que pida dos palabras, las pase como parámetro a un 
# procedimiento y determine si riman o no. Si coinciden las tres últimas letras, 
# debe decir que riman. Si coinciden solo las dos últimas, debe decir que riman 
# un poco, y si no coinciden, que no riman.

def compruebaRima(texto1, texto2):
    caracteres1 = texto1[-3:]
    caracteres2 = texto2[-3:]

    if caracteres1 == caracteres2:
        print(f'Las palabras {texto1} y {texto2} riman.')

    elif caracteres1[1:] == caracteres2[1:]:
        print(f'Las palabras {texto1} y {texto2} riman un poco.')

    else:
        print(f'Las palabras {texto1} y {texto2} no riman.')


palabra1 = input('Escribe una palabra: ')
palabra2 = input('Escribe otra palabra: ')

compruebaRima(palabra1, palabra2)