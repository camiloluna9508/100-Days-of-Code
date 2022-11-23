travel_log = [
{
"country": "France",
"visits":12,
"cities": ["Paris", "Lille", "Dijon"]
},
{
"country": "Germany",
"visits":5,
"cities": ["Berlin", "Hamburg", "Stuttgart" ]
}
]

def agregar_pais(x):
    pais =input("Ingresa el nombre del pais que visitaste: ")
    num = int(input("Ingresa el numero de visitas que hiciste: "))
    ciudades = []
    autoridad = True
    while (autoridad==True):
        ciudades.append(input("En que ciudad estuvo: "))
        autoridad=seguir(input("Desea ingresar otra ciudad (Si/No): ").upper())
    new = {
            "country":pais,
            "visits":num,
            "cities":ciudades
        }
    x.append(new)

def seguir(x):
    if (x=="SI"):
        return True
    else:
        return False
    

agregar_pais(travel_log)
print(travel_log)