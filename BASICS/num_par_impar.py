#Ingresar un número y mostrar si el número ingresado es par o impar. Todo número par es divisible por dos.
num=int (input("Por favor ingrese un número para determinar si es par o impar"))
if (num%2==0):
    print ("El número ",num," es par")
else:
    print ("El número ",num," es impar")