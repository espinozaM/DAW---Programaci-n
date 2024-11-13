'''
Escribir un programa para jugar a adivinar un número (el usuario piensa un número y el programa lo ha de adivinar).
El programa empieza pidiendo entre qué números está el número a adivinar y luego intenta adivinar de qué número
se trata. El usuario va diciendo si el número que ha dicho el programa es menor, mayor o igual al que se ha buscado.
Valor mínimo: 0
Valor máximo: 100
Piensa un número entre 0 y 100 a ver si lo puedo adivinar.
Es 50 ?: mayor
Es 75 ?: menor
Es 62 ?: menor
Es 56 ?: mayor
Es 59 ?: igual
Gracias por jugar!!
Mejoras (opcionales):
    • que al principio el programa se asegure de que el valor máximo es superior al valor mínimo.
    • Que el programa detecte "trampas", por ejemplo, si cuando dices "25" le decimos "mayor" y al decir "26"
    le decimos "menor", el programa debe decir que estamos haciendo trampas y debe dejar de jugar con nosotros.
'''

import random
import time

minimo = int (input ( "Valor mínimo: "))
max = int (input ( "Valor máximo: "))

while max <= minimo:
    max = int (input ( f"El número debe ser mayor que {minimo}. Valor máximo: "))

print(f'Piensa un número entre {minimo} y {max} a ver si lo puedo adivinas.')

botChoice = random.randint (minimo, max)
userInput = ""

while userInput != "igual":
    userInput = input(f'Es {botChoice} ?: ').lower()
    if userInput == 'mayor':
        minimo = botChoice + 1
    elif userInput == 'menor':
        max = botChoice - 1
    
    botChoice = random.randint (minimo, max)

print('Gracias por jugar!!')
