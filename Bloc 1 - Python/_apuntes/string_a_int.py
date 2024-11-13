

def strToInt(numStr):
    # Lista con números del 1 al 9 como cadenas de texto
    lista = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    numInt = 0

    # for digito in numStr:
    for j in range(len(numStr)):
        found = False
        i = 0
        while not found and i < len(lista):
            if numStr[j] == lista[i]:
                found = True
                numInt += i * 10 ** ((len(numStr) - 1) - j)
            else:
                i += 1

    return numInt

resultado = strToInt('100') + strToInt('100')

print(resultado)
