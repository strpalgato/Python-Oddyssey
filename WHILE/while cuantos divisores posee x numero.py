import os
os.system("cls") #limpiando la terminal
#ingresar un numero y mostrar los divisores del numero ingresado
num=int (input("Ingrese un numero positivo para determinar todos los divisores que posee"))
i=1 #contador de vueltas
while (i<=num):
    if (num%i==0):
        print (i, " es divisor de ",num)
    i+=1    
