alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Quieres 'Incriptar' tu texto o, 'Desincriptar':\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def encrypt(text,shift,direction):
    if direction=="incriptar":
        direction="Codificado"
    else:
        direction="Descodificado"
        shift=-shift
    text=list(text)
    for i in range (len(text)):
        if text[i]==" ":
            text[i]=" "
        else:
            indice=alphabet.index(text[i])
            text[i]=alphabet[indice+shift]
    print(f"Tu texto {direction} es: ","".join(text))

encrypt(text,shift,direction)