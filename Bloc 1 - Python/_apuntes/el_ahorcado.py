import random

def dibujar(num_intents):
    print('\n'*99)
    print("__________")
    print("|        |")
        
    if num_intents == 0:
        print("|")
        print("|")
        print("|")
    else:
        if num_intents == 1:
            print("|        O")
            print("|")
            print("|")
        else:
            if num_intents == 2:
                print("|        O")
                print("|        |")
                print("|")
            else:
                if num_intents == 3:
                    print("|        O")
                    print("|       /|")
                    print("|")
                else:
                    if num_intents == 4:
                        print("|        O")
                        print("|       /|\ ")
                        print("|")
                    else:
                        if num_intents == 5:
                            print("|        O")
                            print("|       /|\ ")
                            print("|       / ")
                        else:
                            if num_intents == 6:
                                print( "|        O")
                                print( "|       /|\ ")
                                print( "|       / \ ")
    print("|")
    print("|___")

num_intentos = 0

palabras_ahorcado = ["pirata", "burro", "truco", "duende", "nieve", "vapor", "fresa", "playa", "miedo", "globo"]

secreto = random.choice(palabras_ahorcado)

#palabra = '_' * len(secreto)
palabra = ['_' for i in secreto]
#palabra = ''
#for letra in secreto:
#    palabra += '_'

palabras_usadas = ''

finalizar = False
while num_intentos < 6 and not finalizar:
    dibujar(num_intentos)

    print(palabra)

    print('Intentos:', num_intentos, '/ 6')
    letra = input('Escribe una letra: ')

    if letra not in secreto or letra in palabras_usadas:
        num_intentos += 1
    else:
        palabras_usadas += letra
        for i in range(len(secreto)):
            if letra == secreto[i]:
                palabra[i] = letra.upper()
        
        if '_' not in palabra:
            finalizar = True


if num_intentos < 6:
    print('Has ganado!!! :)')
    print(palabra)
else:
    dibujar(6)
    print('Has perdido! :(')
    print('La palabra es:', secreto)