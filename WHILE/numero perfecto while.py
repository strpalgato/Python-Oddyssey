#Ingresar un numero y mostrar si el numero ingresado es Perfecto o no lo es. 
#Un numero es perfecto cuando la suma de sus divisores (sin contar el mismo numero) da como resultado el mismo numero
#Ejemplo: 6 es perfecto, sus divisores son 1, 2, 3, 6, si sumo 1+2+3=6  6=6
#Ejemplos para test: Los primeros 8 numeros perfectos (6 , 28 , 496 , 8128 , 550.336 , 589.869.056 , 438.691.328 , 2.305.843.008.139.952.128)
import os
os.system("cls") #limpiando la terminal

i=1 #contador de vueltas
num=int (input("Por favor, ingrese un numero para determinar si es perfecto"))
sumadivisor=0
while (i<num):
    resto=num%i
    if (resto==0):
        sumadivisor+=i
    i+=1
if (num==sumadivisor):
    print ("El numero {} es perfecto".format(num))
else:
    print ("El numero {} no es perfecto".format(num))