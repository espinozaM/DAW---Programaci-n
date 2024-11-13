
'''
Pida un número que como máximo tenga tres cifras (por ejemplo 
serían válidos 1, 99 i 213 pero no 1001). Si el usuario introduce 
un número de más de tres cifras debe informar con un mensaje 
de error como este “ERROR: El número 1005 tiene más de tres cifras”.

'''

n = float(input('Introduce un número: '))

if n<=999 and n>=0.00:
    print('CORRECTO: El número tiene menos de tres cifras')
else:
    print('El número es incorrecto')