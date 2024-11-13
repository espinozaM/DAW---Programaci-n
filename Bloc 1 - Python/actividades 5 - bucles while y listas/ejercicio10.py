'''
Escribe un programa que te pida los nombres y notas de alumnos. Si escribes una nota fuera del intervalo
de 0 a 10, el programa entenderá que no quieres introducir más notas de este alumno. Si no escribes el nombre,
el programa entenderá que no quieres introducir más alumnos.
Nota: La lista en la que se guardan los nombres y notas tiene esta estructura
[[nombre1, nota1, nota2, etc], [nombre2, nota1, nota2, etc], [nom3, nota1, nota2, etc], etc]
Dame un nombre: Héctor Quiroga
Escribe una nota: 4
Escribe otra nota: 8.5
Escribe otra nota: 12
Dame otro nombre: Inés Valls
Escribe una nota: 7.5
Escribe otra nota: 1
Escribe otra nota: 2
Escribe otra nota: -5
Dame otro nombre:
Las notas de los alumnos son:
Héctor Quiroga: 4.0 - 8.5
Inés Valls: 7.5 - 1.0 - 2.0
'''

notas_alumno = []

parar = False

while parar == False:
    nombre = input('Dame un nombre: ')
    if nombre == "":
        parar = True
    else:
        nota = float(input('Escribe una nota: '))
        notas = []

        while 0 <= nota <= 10:
            notas.append(nota)
            nota = float(input('Escribe otra nota: '))
            
        notas_alumno.append([nombre] + notas)

print(notas_alumno)
print('Las notas de los alumnos son:')
for alumnoInfo in notas_alumno:
    nombre = alumnoInfo[0]
    notas = alumnoInfo[1:]

    notasStr = ''
    for i in range(len(notas)):
        separador = ' - '
        if i == 0 or i == len(notas):
            separador = ''
        notasStr += separador + str(notas[i])

    print(f'{nombre}: {notasStr}')
