#La señora Juanita, es dueña de 5 carros que venden sopaipillas en la calle
#Necesita un programa que le permita manejar de las ventas de cada uno de ellos.
#Se debe utilizar una matriz de 5x7, 5 filas y 7 columnas, las filas representarán cada uno de los carros
#y las columnas, cada dia de la semana.

from os import system
system("cls")
import numpy as np
import random
num=0
n=5
m=7

while(True):
    print("Escoja una de las siguientes opciones: ")
    print("1. Llenar la matriz")
    print("2. Mostrar todo")
    print("3. Mostrar especifico")
    print("4. Mayor y menor")
    print("5. Arreglo")
    print("6. Salir")
    try:
        opcion=int(input(""))
        if(opcion!=1) and (opcion!=2) and (opcion!=3) and (opcion!=4) and (opcion!=5) and (opcion!=6):
            print("Error, solamente se pueden escoger las opciones mostradas.")
            continue
        if(opcion==1):
            print("A continuacion, se introduciran los valores a la matriz.")
            print("Valores introducidos exitosamente.")
            matriz=np.empty((n,m)) #defino una matriz de n por n
            for i in range(n):
                for j in range (m):
                    while(True):
                        num=random.randrange(3000, 50000)
                        break
                    matriz[i,j]=num #matriz [i][j]=num

        if(opcion==2) and (num==0):
            print("Usted no puede realizar esta acción hasta que ejecute la opción 1.")
        elif(opcion==2) and (num>=3000):
            for i in range(n):
                for j in range(m):
                    print(matriz[i,j])
                print()
            print(matriz)

        if(opcion==3) and (num==0):
            print("Usted no puede realizar esta acción hasta que ejecute la opción 1.")
        elif(opcion==3) and (num>=3000):
            while(True):
                try:
                    carrito=int(input("Ingrese el numero de carrito: "))
                    if (carrito>0) and (carrito>6):

                        break
                    else:
                        print("Debe introducir un numero positivo del 1 al 5")
                except ValueError:
                    print("Debe introducir un numero entero")
        if(opcion==6):
            break
    except ValueError:
        print("Debe escoger una de las opciones mostradas")
        continue
print("Usted a salido del programa.")