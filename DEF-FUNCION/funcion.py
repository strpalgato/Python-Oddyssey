import os
def sumaDos():
    suma=0
    while(True):
        try:
            num1=int(input("Ingrese un numero: "))
            break
        except ValueError:
            print("Error, debe ingresar un numero entero.")
    while(True):
        try:
            num2=int(input("Ingrese un numero: "))
            break
        except ValueError:
            print("Error, debe ingresar un numero entero.")
    suma=num1+num2
    print("La suma es: {}".format(suma))

def sumaDos1():
    suma=0
    while(True):
        try:
            num1=int(input("Ingrese un numero: "))
            break
        except ValueError:
            print("Error, debe ingresar un numero entero.")
    while(True):
        try:
            num2=int(input("Ingrese un numero: "))
            break
        except ValueError:
            print("Error, debe ingresar un numero entero.")
    suma=num1+num2
    return suma

# aqui comienza el main o programa principal.
print("Ejemplo de funciones")
sumaDos()
# funcion que retorna la suma.
aa=sumaDos1()
print("La suma es {}".format(aa))