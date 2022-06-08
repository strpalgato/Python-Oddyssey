import os
os.system("cls") #limpiando la terminal
#Ingresar 10 números y mostrar: Cuantos son positivos y cuantos son negativos.

i=1 #contador de vueltas
contnum=0
contnumnegativo=0
while (i<=10):
    print ("Numero : ",i)
    num=int (input("Ingrese un numero positivo o negativo"))
    if (num>0):
        contnum+=1
    else: 
        contnumnegativo+=1
    i+=1
print ("Los numeros positivos ingresados corresponden a : ",contnum)
print ("Los numeros negativos ingresados corresponden a : ",contnumnegativo)