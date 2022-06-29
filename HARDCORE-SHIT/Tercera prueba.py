from os import system
system("cls")
import numpy as np

def menu(): # muestra el menú de opciones
    print("D E V I A N T")
    print("**************************************")
    print("1. Mostrar camarotes disponibles")
    print("2. Comprar pasaje")
    print("3. Totales")
    print("4. Anular venta")
    print("5. Listado de pasajeros")
    print("6. Salir")
    print()

def opcion3(): # imprime la boleta de ganancias al seleccionar la opcion 3
    print("----------------------------------------------")
    print("Cantidad de camarotes Vip vendidos: {}".format(vip))
    print("Cantidad de camarotes Normales vendidos: {}".format(normal))
    print("Cantidad de camarotes Premium vendidos: {}".format(premium))
    print("Total recaudado: ${}".format(ganancias))
    input("Presione 'enter' para continuar...")

def ordenar_id(): # ordena las id de los pasajeros en la opcion 5 si es que se cumplen las condiciones
    print("A continuación se mostrará la lista de pasajeros ordenada de menor a mayor según su id: ")
    for recorrido in range(1,len(id_pasajero)): # ciclo for para ordenar la lista de menor a mayor
        for posicion in range(len(id_pasajero)-recorrido):
            if id_pasajero[posicion]>id_pasajero[posicion+1]:
                temp=id_pasajero[posicion]
                id_pasajero[posicion]=id_pasajero[posicion+1]
                id_pasajero[posicion+1]=temp
    print(id_pasajero) # se imprime la lista de menor a mayor

id_pasajero=[] # lista pasajeros
asientosV=[] # lista de asientos que se venden con su respectivo numero
camarote=0 # contador matriz
ganancias=0 # contador de dinero
vip=0 # contador de asientos vip vendidos
premium=0 # contador de asientos premium vendidos
normal=0 # contador de asientos normales vendidos

while(True): # creacion de matriz
    matriz=np.empty((6,6))
    for i in range(6):
        for j in range(6):
            while(True):
                camarote+=1
                break
            matriz[i,j]=camarote
    break

while(True): # menú
    c=0
    menu()
    try:
        opcion=int(input("Elija una de las opciones: "))
        if(opcion!=1) and (opcion!=2) and (opcion!=3) and (opcion!=4) and (opcion!=5) and (opcion!=6):
            print("Error, solamente se pueden escoger las opciones mostradas.")
            continue
        if(opcion==1): # imprime la matriz
            print(matriz)
            print()
        if(opcion==2): # proceso de venta
            while(True):
                try:
                    compra=int(input("Seleccione el asiento que desea comprar para verificar si está disponible: "))
                    if(compra>=1) and (compra<=36):
                        if compra in asientosV: # si el programa verifica que el asiento ya se encuentra en la lista (de asientos vendidos), no realiza la venta.
                            print("Este asiento ya ha sido comprado, por lo tanto no se encuentra disponible. (volviendo al menú)")
                            break
                        while(True):
                            if(compra==1) or (compra==8) or (compra==15) or (compra==22) or (compra==29) or (compra==36):
                                print("El valor de este asiento es de $300 barras de latinio prensado (VIP)")
                            elif(compra==6) or (compra==11) or (compra==16) or (compra==21) or (compra==26) or (compra==31):
                                print("El valor de este asiento es de $200 barras de latinio prensado (PREMIUM)")
                            else:
                                print("El valor de este asiento es de $100 barras de latinio prensado (NORMAL)")
                            try:
                                confirmacion=input("¿Desea comprar este asiento? (S=Comprar / N=Escoger otro): ").upper()
                                if(confirmacion=="N"):
                                    break
                                elif(confirmacion=="S"):
                                    while(True):
                                        try:
                                            rut=int(input("Ingrese su rut completo, sin puntos ni guión (ejemplo: 214757921): "))
                                            rut=str(rut)
                                            if len(rut)==9:
                                                id_pasajero.append(rut)
                                                break
                                            else:
                                                print("No se han introducido 9 dígitos")
                                        except ValueError:
                                            print("ERROR: Debe introducir solo numeros enteros y el rut debe tener una extension de 9 dígitos.")
                                    asientosV.append(compra)
                                    matriz[matriz==compra] = -1
                                    if(compra==1) or (compra==8) or (compra==15) or (compra==22) or (compra==29) or (compra==36):
                                        vip+=1
                                        ganancias+=300
                                        print("Compra realizada exitosamente, volviendo al menú.")
                                    elif(compra==6) or (compra==11) or (compra==16) or (compra==21) or (compra==26) or (compra==31):
                                        premium+=1
                                        ganancias+=200
                                        print("Compra realizada exitosamente, volviendo al menú.")
                                    else:
                                        normal+=1
                                        ganancias+=100
                                        print("Compra realizada exitosamente, volviendo al menú.")
                                    break
                                else:
                                    print("Solamente debe escoger las opciones S/N para continuar.")
                                    continue
                            except ValueError:
                                print("ERROR: Debe escribir 'S' para comprar o 'N' para escoger otro.")
                            break
                    else:
                        print("Debe seleccionar un asiento que este disponible (del 1 al 36)")
                        continue
                except ValueError:
                    print("ERROR: Seleccione un asiento disponible (numero entero)")
                    continue
                break
        if(opcion==3):
            opcion3()
            continue
        if(opcion==4):
            while(True):
                try:
                    anular=int(input("Ingrese el numero del asiento que desea restaurar: "))
                    if(anular>=1) or (anular<=36):
                        print()
                        if anular in asientosV:
                            while(True):
                                try:
                                    reembolso=input("Este asiento posee propietario, ¿desea restaurarlo? (S=restaurar / N=Seleccionar otro): ").upper()
                                    if reembolso=="S":
                                        while(True):
                                            if(anular==1) or (anular==8) or (anular==15) or (anular==22) or (anular==29) or (anular==36):
                                                pos=asientosV.index(anular)
                                                id_pasajero.pop(pos)
                                                asientosV.remove(anular)
                                                matriz[matriz==-1]=anular
                                                vip-=1
                                                ganancias-=300                                               
                                                matriz.sort(axis=1)
                                                print("Compra anulada exitosamente, volviendo al menú")
                                                break
                                            elif(anular==6) or (anular==11) or (anular==16) or (anular==21) or (anular==26) or (anular==31):
                                                pos=asientosV.index(anular)
                                                id_pasajero.pop(pos)
                                                asientosV.remove(anular)
                                                matriz[matriz==-1]=anular
                                                premium-=1
                                                ganancias-=200
                                                print("Compra anulada exitosamente, volviendo al menú")
                                                break
                                            else:
                                                pos=asientosV.index(anular)
                                                id_pasajero.pop(pos)
                                                asientosV.remove(anular)
                                                matriz[matriz==-1]=anular
                                                normal-=1
                                                ganancias-=100
                                                print("Compra anulada exitosamente, volviendo al menú")
                                                break
                                    elif reembolso=="N":
                                        break
                                    else:
                                        print("Solo se puede seleccionar 'S' o 'N'")
                                except ValueError:
                                    print("ERROR: Debe seleccionar los caracteres mencionados (S/N)")
                                break
                    else:
                        print("Debe seleccionar un asiento del 1 al 36.")
                except ValueError:
                    print("ERROR:Debe seleccionar un asiento en numeros enteros.")
                break
                
        if(opcion==5):
            lenlista=len(id_pasajero)
            if(lenlista==0):
                print("En estos momentos no se encuentra ningun pasajero registrado en la lista.\nNo existen ventas...")
                continue
            else:
                ordenar_id()
                continue
        if(opcion==6):
            print("¡Que tenga un excelente día!")
            print("P R O G R A M A  F I N A L I Z A D O")
            break
    except ValueError:
        print("ERROR: Debe introducir un numero entero.")
        continue