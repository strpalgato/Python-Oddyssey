#Ingresar dos números entero y luego determinar y mostrar: 
#Si el primero es divisible por el segundo 
#Si el segundo es divisible por el primero 
#Cuál de los dos es mayor; en caso que sean iguales, mostrar mensaje adecuado 

num1=int (input("Por favor, ingrese el primer número"))
num2=int (input("Por favor ingrese el segundo número"))
mod=num1%num2
mod2=num2%num1
if (num1%num2==0):
    print ("El primer número es divisible por el segundo, ya que no sobra resto. ",num1," % ",num2," = ",mod)
else:
    print ("El primer número no es divisible por el segundo, ya que sobra resto. " ,num1," % ",num2," = ",mod)

if (num2%num1==0):
    print ("El segundo número es divisible por el primero, ya que no sobra resto. ",num2," % ",num1," = ",mod2)
else:
    print ("El segundo número no es divisible por el primero, ya que sobra resto. ",num2," % ",num1," = ",mod2)

if (num1>num2):
    print ("El número ",num1," es mayor que el número ",num2)
elif (num1<num2):
    print ("El número ",num1," es menor que el número ",num2)
else:
    print ("El número ",num1," y ",num2," son iguales")