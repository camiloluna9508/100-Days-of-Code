import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Bienvenido al generador de contraseñas!")
num_le = int(input("Cuantas letras desea incluir en su contraseña?: "))
num_num = int(input("Cuantos numeros desea incluir en su contraseña?: "))
num_sim = int(input("Cuantos simbolos desea incluir en su contraseña?: "))
password = []
for l in range (1,num_le+1):
    password.append(random.choice(letters))
for n in range (1,num_num+1):
    password.append(random.choice(numbers))
for s in range (1,num_sim+1):
    password.append(random.choice(symbols))
random.shuffle(password)
print("Tu contrasela es: ","".join(password))
