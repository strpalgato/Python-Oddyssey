#Ejercicio en clases python 1 pero con WHILE
#Upper transforma a mayuscula y lower a minusculas

import os
os.system("cls") #limpiando la terminal

i=1 #contador de vueltas
contHombre=0 #valor inicial a los contadores, va a partir de 0
contMujer=0 #valor inicial a los contadores, va a partir de 0
while(i<=5):
    print ("Persona ",i)
    edad1=int (input("Ingrese la edad de la persona"))
    gen1=input("Ingrese el genero del la persona (F:femenino/M:masculino)").upper()
    if (gen1=="F"):
        contMujer+=1
    else:
        contHombre+=1
    i+=1
print ("El total de mujeres es : ",contMujer)
print ("El  total de hombres es :",contHombre)