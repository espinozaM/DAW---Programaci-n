'''
Pida al usuario tres número que serán el día, mes y año. Comprueba que la fecha introducida es válida.  Por ejemplo: 
32/01/2017->Fecha incorrecta
29/02/2017->Fecha incorrecta
30/09/2017->Fecha correcta.
'''

# Días máximos de cada mes en un año no bisiesto
dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

dia = int(input('Dia: '))
mes = int(input('Mes: '))
any = int(input('Any: '))

if any > 0:  # Verifica que el año sea mayor que 0
    if mes == 1 and dia > 0 and dia <= 31:
        print('Fecha correcta')
    elif mes == 2:
        # Verificar si es un año bisiesto
        if ((any % 4 == 0 and any % 100 != 0) or (any % 100 and any % 400 == 0)):  # Año bisiesto
            if dia > 0 and dia <= 29:
                print('Fecha correcta')
            else:
                print('Día incorrecto para febrero en un año bisiesto')
        else:  # Año no bisiesto
            if dia > 0 and dia <= 28:
                print('Fecha correcta')
            else:
                print('Día incorrecto para febrero en un año no bisiesto')
    elif mes == 3 and dia > 0 and dia <= 31:
        print('Fecha correcta')
    elif mes == 4 and dia > 0 and dia <= 30:
        print('Fecha correcta')
    elif mes == 5 and dia > 0 and dia <= 31:
        print('Fecha correcta')
    elif mes == 6 and dia > 0 and dia <= 30:
        print('Fecha correcta')
    elif mes == 7 and dia > 0 and dia <= 31:
        print('Fecha correcta')
    elif mes == 8 and dia > 0 and dia <= 31:
        print('Fecha correcta')
    elif mes == 9 and dia > 0 and dia <= 30:
        print('Fecha correcta')
    elif mes == 10 and dia > 0 and dia <= 31:
        print('Fecha correcta')
    elif mes == 11 and dia > 0 and dia <= 30:
        print('Fecha correcta')
    elif mes == 12 and dia > 0 and dia <= 31:
        print('Fecha correcta')
    else:
        print('Mes o día incorrecto')
else:
    print('Año incorrecto')


'''
if any > 0:
    # comprueba año bisiesto
    if (any % 4 == 0 and any % 100 != 0) or (any % 400 == 0):
        dias_por_mes[1] += 1

    # comprueba dia del mes
    if dia > 0 and dia <= dias_por_mes[mes-1]:
        print('dia correcto')
        if mes > 0 and mes <= 12:
            #print('mes correto')
            print('la fecha es correcta')
        else:
            print('La fecha es incorrecta')

'''

