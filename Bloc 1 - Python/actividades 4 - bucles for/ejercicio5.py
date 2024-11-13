'''
Escribe un programa que pida la altura y ancho de un rectángulo y lo dibuje de la siguiente manera:
Anchura del rectángulo: 5
Altura del rectángulo: 3
*****
*****
*****

'''
alto = int(input('Escribre la altura: '))
ancho = int(input('Escribe el ancho: '))

#dibujo = ''
for i in range(alto):
    #print('*' * ancho)
    for i in range(ancho):
        print('*', end='')
    print('\n')
    
    #for x in range(ancho):
    #    dibujo += '*'
    #dibujo += '\n'
#print(dibujo)

    
