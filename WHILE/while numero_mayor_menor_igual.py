#Ingresar dos números enteros y mostrar cual de los dos números es mayor. Si los números son iguales verificarlo.
num1=int (input("Por favor ingrese el primer número entero"))
num2=int (input("Por favor ingrese el segundo número entero"))
if (num1>num2):
    print ("El número ",num1," es mayor que el número ",num2)
elif (num1<num2):
    print ("El número ",num1," es menor que el número ",num2)
else:
    print ("El número ",num1,"y el número ",num2," son iguales")