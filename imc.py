print("Calculemos tu indice de masa corporal")
peso=float(input("Ingresa tu peso en Kilogramos: "))
estatura=float(input("Ingresa tu estatura en Metros: "))
ibm=peso/(estatura**2)
print(ibm)
x=[18.5,24.9,29.9,34.9,40]
indice=["Bajo Peso","Peso Normal","Sobrepeso","Obesidad grado 1","Obesidad grado 2","Obesidad grado 3--obesidad mórbida"]
i=0
while i<len(x):
    if (ibm<x[i]):
        print(indice[i])
        i=len(x)
    elif ibm>x[-1]:
        print(indice[-1])
    else:
        i+=1