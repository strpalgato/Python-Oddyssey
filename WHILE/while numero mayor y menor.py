import os
os.system("cls") #limpiando la terminal
#Ingresar 10 numeros y mostrar el mayor y el menor

i=1 #Contador de vueltas
while (i<=10):
    print ("Numero : ",i)
    num=int (input("Ingrese un numero"))
    if(i==1):
        mayor=num
        menor=num
    if (num>mayor):
        mayor=num
    if (num<menor):
        menor=num   
    i+=1
print ("el numero mayor es ",mayor)
print ("el numero menor es ",menor)