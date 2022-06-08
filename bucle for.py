#Escribir un programa que pregunte al usuario su edad y
#años que ha cumplido (desde 1 hasta su edad).
age = int(input("¿Cuantos años tiene? "))
for i in range (age):
    print("has cumlpido " + str (i+1) + " años")

#Escribir un programa que pida al usuario un número entero
#positivo y muestre por pantalla todos los números impares
#desde 1 hasta ese número separados por comas.

n=int(input("Introduce un número entero positivo: "))
for i in range (1, n+2, 2):
    print(i, end=",")

#Actividad
#Escribir un programa que pida al usuario una palabra y luego
#muestre por pantalla una a una las letras de la palabra
#empezando por la última.
print("")
palabra=input("Por favor, introduzca una palabra: ")

str = palabra
palabra=''.join(reversed(str))

for x in palabra:
    print(x)