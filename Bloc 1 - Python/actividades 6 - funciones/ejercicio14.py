'''
Aprovechando el potencial de los diccionarios, escribe un programa que llame a un procedimiento,
que recibe como parámetro la fecha en números y devuelve la fecha  con el nombre del mes.
Comentario: no es necesario validar si la es correcta, damos por hecho que lo será. 

>>>
Introduce una fecha en formato dd/mm/aaaa: 02/11/2019
02 de noviembre de 2019
'''

def formatearFecha(fecha):
    meses = {
        1: 'Enero',
        2: 'Febrero',
        3: 'Marzo',
        4: 'Abril',
        5: 'Mayo',
        6: 'Junio',
        7: 'Julio',
        8: 'Agosto',
        9: 'Septiembre',
        10: 'Octubre',
        11: 'Noviembre',
        12: 'Diciembre'
    }
    
    # 02/11/2019
    dia = fecha[:2]
    mes = fecha[3:5]
    anio = fecha[6:]

    return f'{dia} de {meses[int(mes)]} de {anio}'

fecha = '02/11/2019'
fechaFormateada = formatearFecha(fecha)

print(fechaFormateada)
