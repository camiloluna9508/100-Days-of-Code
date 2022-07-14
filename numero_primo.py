def primo(x):
    is_primo=True
    for i in range (2,x):
        if x%i==0:
            is_primo=False
    print(f"El numero {x} es primo:",is_primo)

x=int(input("ingresa el numero: "))
primo(x)
