# Pida al usuario el espacio recorrido por un coche y el tiempo que
# ha tardado en horas y que calcule a qué velocidad media había
# realizado el recorrido.

recorrido = int(input('Introduce recorrido: '))
tiempo = int(input('Introduce el tiempo que ha tardado en horas: '))

velocidadMedia = int(recorrido / tiempo)

print('La velocidad media ha sido de:', velocidadMedia, 'km/h')