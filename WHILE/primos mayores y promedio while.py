#Ingresar N números y mostrar:
#Total de números primos ingresados (contador primos)
#Total de números mayores a 10 y menores a 50 (contador rango)
#Promedio de números entre 50 y 70 (contador rango 2)

import os
os.system("cls") #limpiando la terminal

cantnum=int (input("Escriba la cantidad de numeros que desea ingresar"))
i=1 #contador de vueltas
contprimos=0
contrango=0
contrango2=0
suma=0

while (i<=cantnum):
    print ("numero : {}".format(i))
    num=int (input("ingrese un numero"))
    if (num>1):
        contcero=0 #contador de ceros   
        i2=2 #recorrido desde el num 2 en adelante (contador de vueltas numero primo)
        while (i2<num) and (contcero==0):
            resto=num%i2
            if (resto==0):
                contcero+=1
            i2+=1    
        if (contcero==0):
            contprimos+=1
    if (num>10) and (num<50):
        contrango+=1
    if (num>=50) and (num<=70):
        contrango2+=1
        suma+=num
    i+=1
promedio=float(suma/contrango2)
print ("El total de numeros primos ingresados es {}".format(contprimos))
print ("El total de numeros mayores a 10 y menores a 50 es {}".format(contrango))
print ("Promedio de los números que se encuentran entre el 50 y el 70 es {}".format(promedio))