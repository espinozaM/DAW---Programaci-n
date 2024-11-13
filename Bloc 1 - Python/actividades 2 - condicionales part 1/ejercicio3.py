#¿Qué función te informa del tipo de dato tiene almacenado una variable? 
# Haz una prueba con los distintos tipos de datos que conoces.

a = 1
b = '1'
c = 1.1
d = [1]
e = (1, 2)
f = True
g = {'clave': 'valor'}
h = None

for i in [a,b,c,d,e,f,g,h]:
    print(type(i))