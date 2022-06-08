from os import system
system("cls")
#randint(a, b)
#Para generar números aleatorios en Python de valor entero, se suele utilizar la función randint(). 
#La función randint(a, b) devuelve un número entero comprendido entre a y b (ambos inclusive) de forma aleatoria. 
import random
comienza = random.randint(0, 1)
if comienza == 0:
    print('Comienza el jugador')
else:
    print('Comienza el PC')