import os
os.system("cls") #limpiando la terminal
#Ingresar 10 numeros y mostrar cuantos son pares y cuantos son impares
print ("Ingresar 10 numeros y determinar cual es par e impar")
i=1 #contador de vueltas
contNum=0
contImpar=0
while (i<=10):
    print ("Numero : ",i)
    num=int (input("Ingrese un numero"))
    if (num%2==0):
        print ("Este numero es par")
        contNum+=1
    else:
        print ("Este numero es impar")
        contImpar+=1
    i+=1    
print ("El total de numeros pares es ",contNum)
print ("El total de numeros impares es ",contImpar)