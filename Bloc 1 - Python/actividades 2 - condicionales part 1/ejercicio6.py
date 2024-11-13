'''
Pida al usuario el precio de un producto y el nombre del producto y 
muestre el mensaje con el precio del IVA (21%). Por ejemplo: 
“Tu bicicleta vale 100 euros y con el 21 % de IVA se queda en 121 euros
 en total”.
'''

precio = int(input('Introduce el precio del producto sin IVA: '))
producto = input('Introduce el nombre del producto: ')
precioConIVA = precio + (precio * 0.21)

print('Tu %s vale %s euros y con el 21 (por ciento) de IVA se queda en %s euros en total.' % (producto, precio, precioConIVA))
