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

import random

print("<<<<<Bienvenido a la tienda DeTodo>>>>>")
while(True):
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
        except:
            print("Error, el producto ingresado no es valido")
            continue
    break