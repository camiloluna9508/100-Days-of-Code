import math
def calculo_latas(ancho,alto,lata):
    x=math.ceil((ancho*alto)/lata)
    print(f"Recuerda que una lata de pintura cubre {lata}:")
    print(f"Necesitaras {x} lastas de pintura.")
a=float(input("ingrese el ancho de la pared que pintara: "))
b=float(input("ingrese el alto de la pared:  "))
c=float(input("ingrese los metros cuadrados que cubre la lata de pintura: "))
calculo_latas(a,b,c)