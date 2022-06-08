import os
os.system("cls") #limpiando la terminal

#Ingresar un número y mostrar los divisores del número ingresado.

num=int (input("Por favor, ingrese un numero para determinar los divisores de este"))
i=1 #contador de vueltas
while (i<=num):
    if (num%i==0):
        print (i,"es divisor de",num)
    i+=1    