#Ingresar dos números. Calcular y mostrar la suma de ambos números. Mostrar adicionalmente mensaje que indique si la suma obtenida es “par” o “impar”.
num1=int (input("Por favor, ingrese el primer número"))
num2=int (input("Por favor, ingrese el segundo número"))
suma=int (num1+num2)

if (suma%2==0):
    print ("la suma es par (",suma,")")
else:
    print ("la suma es impar (",suma,")")