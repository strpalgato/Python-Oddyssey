from os import system
system("cls")
#randrange(a, b, salto)
#La función randrange(a, b, salto) genera números enteros aleatorios comprendidos entre a y b separados entre sí con un salto. 
#Por ejemplo, randrange(5, 27, 4) obtendría un valor aleatorio de entre los siguientes posibles: 5, 9, 13, 17, 21, 25.
import random
i=1
while(i<=10):
    print(random.randrange(5, 27, 4))
    i+=1