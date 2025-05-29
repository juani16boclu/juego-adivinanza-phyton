import random

numero_secreto = random.randint(1,100)
cantidad_intentos = 0
cant_max_int = 8
adivinado = False

print("¡Bienvenido al juego de aviniar el numero secreto!")

while not adivinado and cantidad_intentos < cant_max_int:
    entrada = input("Introduce un número del 1 al 99: ")
    numero = int(entrada)
    if numero == numero_secreto:
     print("¡Felicitaciones, adivinaste el numero secreto!")
     adivinado = True
    elif numero < numero_secreto:
     print("El numero es mayor al ingresado")
    else:
     print("El numero es menor al ingresado")
    
    cantidad_intentos += 1

if not cantidad_intentos < cant_max_int:
  print("¡GAME OVER!")