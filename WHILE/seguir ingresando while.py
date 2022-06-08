#Ingresar números, el ingreso deberá finalizar cuando el usuario no quiera seguir ingresando. 
#Se pide sumar los números pares y mostrar el total de números perfectos.
import os
os.system("cls") #limpiando la terminal

#contador de vueltas numero perfecto
suma=0
perfect=0
while True:
    i=1
    sumadivisor=0
    num=int (input("Ingrese un numero: "))
    while (i<num):
        resto=num%i
        if (resto==0):
            sumadivisor+=i
        i+=1
    if(num%2==0):
        suma+=num 
    if(num==sumadivisor):
        perfect+=1       
    respuesta=input("Desea ingresar otro numero? (si=S/no=N): ")
    if(respuesta=="S") or (respuesta=="s"):
        continue
    if(respuesta=="N") or (respuesta=="n"):
        break    
print("El resultado de la suma total de los numeros pares corresponde a: {}".format(suma))
print("El total de los numeros que son perfectos corresponde a: {}".format(perfect))