

evaluacion = []
alumne = []

nota = []

nom = input("Introdueix el nom de l'alumne: ")

while nom != '':
    notaInput = float(input('Introduce una nota: '))
    nota.append(notaInput)

    while 0<= nota[-1] <= 10:
        notaInput = float(input('Introdueix una altra nota: '))
        nota.append(notaInput)

    nota.pop()
    alumne= [nom] + nota #[:] # cuando concatenas listas, se crea una nueva lista y ya no apunta la misma direccion de memoria

    # cuando se asigna una lista a otra variable, esta sigue apuntando a la misma direccion de memoria
    # por lo que cualquier cambio en la lista original, afecta a la variable actual
    # alumne[:] copia el contenido de alumne, no la direccion de memoria
    evaluacion += [alumne[:]] 


    nom = input("Introdueix el nom de l'alumne: ")
    # elimina el contenido de la variable nota
    del nota[:]
    #nota = []

    # del variable eliminaria la variable
    

for i in evaluacion:
    print(i)