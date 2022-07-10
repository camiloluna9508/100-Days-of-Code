import random
x=["Piedra","Papel","Tijeras"]
figura= ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
,
'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
,
 '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]
print("Hola, Jugaremos al famoso juego piedra papel o tijeras...")
i=1
while i==1:
  player=int(input("Elige 1-Piedra, 2-Papel, 3-Tijeras: "))
  player=player-1
  print("Player:",x[player],figura[player])
  cpu=random.choice(x)
  print("CPU:",cpu,figura[x.index(cpu)])
  cpu=x.index(cpu)
  if player==0 and cpu==2:
    print("GANASTE :)")
  elif player==2 and cpu==0:
    print("PERDISTE :(")
  elif cpu>player:
    print("PERDISTE :(")
  elif player>cpu:
    print("GANASTE :)")
  elif player==cpu:
    print("Fue un empate ")
  elif player<0 and player>2:
    print("El numero que ingreso no es valido")
  i=int(input("Quieres seguir jugando ingresa 1, si tu respuesta es no ingresa cualquier otro numero"))