import os
os.system("cls") #limpiando la terminal
#Ingresar 10 numeros y mostrar la suma de los numeros mayores a 30 ingresados
i=1 #contador de vueltas
sumanum=0
while (i<=10):
    print ("Numero ",i)
    num=int (input("Ingrese un numero"))
    if (num>30):
        print ("El numero ",num," es mayor a 30")
        sumanum+=num
    i+=1    
print ("La suma total de los numeros mayores a 30 es ",sumanum)