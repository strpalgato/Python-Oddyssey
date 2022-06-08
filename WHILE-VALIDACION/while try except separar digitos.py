print("Separar digitos")
b=0
sw=False
while(not sw):
    try:
        n=int(input("Ingrese un numero entero positivo: "))
        if (n>0):
            sw=True
        else:
            print("El numero debe ser positivo ")
    except ValueError:
        print("Error, debe ingresar un numero")
cont=0
while(n>0):
    b=n%10 #rescato el ultimo digito
    n=n//10 #division entera, para achicar el numero
    cont+=1 #cuento cada digito
    print("Digito ",b) #mostrando cada digito
print("La cantidad de digitos es: ",cont)
#traza
#   sw      n       cont    b
#   False   123     0       3       123%10=3    123//10=12
#   true    12      1       2       12%10=2     12//10=1                 