import os
os.system("cls") #limpiando la terminal

#Ingresar un número y mostrar si el número ingresado es primo o no lo es.  Un número primo solo es divisible por 1 y por sí mismo, por ningún otro número más.

num=int (input("Por favor, ingrese un numero para determinar si es primo o compuesto"))
if (num>1):
    cont=0 #contador de ceros   
    i=2 #recorrido desde el num 2 en adelante (contador de vueltas)
    while (i<num) and (cont==0):
        resto=num%i
        if (resto==0):
            cont+=1
        i+=1
    if (cont==0):
        print ("El {} es un numero primo".format(num))
    else:
        print ("El {} no es un numero primo".format(num))
else:
    print ("El {} no es un numero primo".format(num))