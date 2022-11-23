estudiantes_notas = {
    "Harry": 88,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

def cambiarnotas(x):
    y={}
    for key in  x:
        if (x[key]>=91 and x[key]<=100):
            y[key]="Excelente"
        elif (x[key]>=81 and x[key]<=90):
            y[key]="Sobresaliente"
        elif (x[key]>=71 and x[key]<=80):
            y[key]="Aceptable"
        else:
            y[key]="Insuficiente"
    return y

estudiantes_notas_grado=cambiarnotas(estudiantes_notas)


print (estudiantes_notas_grado)