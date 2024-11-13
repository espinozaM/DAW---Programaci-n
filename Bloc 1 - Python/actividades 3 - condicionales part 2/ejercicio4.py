# Pida al usuario tres números y un cuarto número, y compruebe si este último es divisor
# de los tres números primeros.

num1 = int(input('Escribe un número: '))
num2 = int(input('Escribe otro número: '))
num3 = int(input('Escribe otro número: '))
divisor = int(input('Escribe un numero divisor: '))

if num1 % divisor == 0 \
    and num2 % divisor == 0 \
    and num3 % divisor == 0:
    print(f'{divisor} es divisor de {num1}, {num2}, {num3}')
else:
    print(f'{divisor} no es divisor de {num1}, {num2}, {num3}')