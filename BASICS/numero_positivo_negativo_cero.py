#Ingresar un número entero y mostrar si dicho numero es positivo, negativo o cero.
num = int (input("Por favor, ingrese un número para determinar si es positivo, negativo o igual a cero"))
if (num > 0):
    print ("El número ingresado ",num," es positivo")
elif (num == 0):
    print ("El número ingresado ",num," es igual a cero")
else:
    print ("El número ingresado ",num," es negativo")