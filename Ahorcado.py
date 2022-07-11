import random
from Arte_Ahorcado import stages,logo,lista_palabras,lose,win
palabra=random.choice(lista_palabras)
vida=6
tamaño_palabra=len(palabra)
display=tamaño_palabra*["_"]
end_game=False
print(logo)
print(stages[vida])
print(display)
while not end_game:
    if (not "_" in display)and(vida>0):
        end_game=True
        print(win)
    elif (vida<1):
        end_game=True
        print("la palabra era: ",palabra)
        print(lose)
    else:
        x=input("adivina una letra:").lower()
        if not x in palabra:
            vida-=1
            print("La ",x," no esta en la palabra")
            print("Pierdes una vida te quedan: ",vida)
            print(stages[vida])
        else:
            for i in range(tamaño_palabra):
                if palabra[i] == x:
                    display[i]=x
            print("La ",x," pertenece a la palabra")
            print(stages[vida])
        print(display)
