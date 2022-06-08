#La tienda "DeTodo" necesita un programa para realizar sus ventas.
#Para esto se le solicita a usted lo siguiente:

#Mostrar 3 productos de la tienda.
#Seleccionar uno de los productos (Ingresando el nombre de producto)
#Mostrar el precio del producto seleccionado.
#Solicitar el monto con el que se desea pagar.
#Visualizar el dinero ingresado al reves.

#Al ingresar un 1 el programa asume que el cliente a finalizado su compra por lo cual
#enviara un mensaje diciendo "adios, muchas gracias por su compra".

#Ademas, dentro del programa existe un sistema de cupones.
#Donde al momento de pagar se enviara un mensaje al cliente.
#Si gano o no un descuento del 5% en su compra (utilizar RANDIT)

from os import system
system("cls")

total=0
valor=0
lista=[]
import random

print("<<<<<Bienvenido a la tienda DeTodo>>>>>")
while(True):
    print("")
    print("Cesta: {}".format(lista))
    print("Valor de la cesta: ${}".format(total))
    print("")
    print("< SELECCION DE PRODUCTOS >")
    print("Ingrese el nombre de uno de los siguientes productos: ")
    while(True):
        print("< MEGADRIVE MINI, FAMICOM MINI, PLAYSTATION CLASSIC >")
        try:
            producto=input().upper()
            if(producto=="MEGADRIVE MINI") or (producto=="FAMICOM MINI") or (producto=="PLAYSTATION CLASSIC"):
                break
            else:
                print("Error, el producto ingresado no es valido")
                continue
        except ValueError:
            print("Error, el producto ingresado no es valido")
            continue
    if(producto=="MEGADRIVE MINI") or (producto=="PLAYSTATION CLASSIC"):
        valor=90000
    if(producto=="FAMICOM MINI"):
        valor=120000
    print("")
    print("Usted a seleccionado {}".format(producto))
    print("Valor a pagar: ${}".format(valor))
    print("")
    print("Desea realizar la compra?: ")
    try:
        print("Escriba '1' para confirmar; '2' para retroceder; '3' para agregar otro producto; '4' para salir.")
        confirmacion=input()
        if(confirmacion=="1"):
            total+=valor
            lista.append(producto)
            descuento=random.randint(1,5)
            print("Usted a comprado: {}".format(lista))
            if(descuento==5):
                print("A recibido un descuento del 5%, felicidades!")
                calculo=total-(0.05*total)
                print("Total: ${}".format(calculo))
            else:
                print("Total: ${}".format(total))
            print("Adios, muchas gracias por su compra.")
            break
        elif(confirmacion=="2"):
            continue
        elif(confirmacion=="3"):
            total+=valor
            lista.append(producto)
            continue
        elif(confirmacion=="4"):
            print("Usted a escogido salir.")
            break
        else:
            print("Solo se admiten los digitos 1, 2, 3 y 4")
    except ValueError:
        print("Solo ingresar los digitos mostrados, no se admiten ni caracteres ni decimales.")
    break