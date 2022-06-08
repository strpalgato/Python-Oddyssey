#Realizar un ejercicio que pida el ingreso de N números, mostrar: 
#Cuantos son positivos
#Cuantos son negativos
#Cuantos son ceros
#La suma de los positivos mayores a 20
#La multiplicación de los negativos menores a -100
#El promedio de los números pares ingresados
# El mayor de todos
# El menor de todos
import os
os.system("cls") #limpiando la terminal
cantnum=int (input("Escriba la cantidad de numeros que desea ingresar: "))
i=1 #contador de vueltas
contpositivo=0
contnegativo=0
contceros=0
contpar=0
sumapar=0
suma=0
multiplicacion=1
while (i<=cantnum):
    print("numero : {}".format(i))
    num=int (input("ingrese un numero entero: "))
    if (num>0):
        contpositivo+=1
    elif (num<0):
        contnegativo+=1
    else:
        contceros+=1       
    if (num>20):
        suma+=num
    if (num<-100):
        multiplicacion*=num
    if (num%2==0):
        contpar+=1
        sumapar+=num
    if(i==1):
        mayor=num
        menor=num
    if (num>mayor):
        mayor=num
    if (num<menor):
        menor=num
    i+=1
promediopar=(sumapar/contpar)
print("El total de numeros positivos ingresados es {}".format(contpositivo))
print("El total de numeros negativos ingresados es {}".format(contnegativo))
print("El total de numeros ceros ingresados es {}".format(contceros))
print("El resultado de la suma total de los numeros positivos mayores a 20 ingresados es {}".format(suma))
print("El resultado de la multiplicacion entre todos los numeros negativos menores a -100 es {}".format(multiplicacion))
print("El promedio de los numeros pares ingresados es {}".format(promediopar))
print("el numero mayor es {}".format(mayor))
print("el numero menor es {}".format(menor))