import os
os.system("cls") #limpiando la terminal
#Ingresar 15 numeros y mostrar la suma de los pares y el total de numeros cero ingresados

i=1 #contador de vueltas
sumapar=0
contcero=0
while (i<=15):
    print ("Numero : ",i)
    num=int (input("Ingrese un numero"))
    if (num%2==0):
        sumapar+=num
    if (num==0):
        contcero+=1
    i+=1
print ("La suma de todos los numeros pares es igual a ",sumapar)
print ("La cantidad de numeros cero ingresados es ",contcero)       