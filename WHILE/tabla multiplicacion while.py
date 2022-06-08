import os
os.system("cls") #limpiando la terminal
#Realizar un programa que me permita mostrar la tabla de multiplicar de un número ingresado. La tabla se mostrará del 1 al 12.
num=int(input("Ingrese un numero para mostrar la tabla: "))
i=1
while(i<=12):
    multi=(num*i)
    print("{} * {} = {} ".format(num,i,multi))
    i+=1