#Ingresar N numeros y luego mostrar:
#Cantidad de numeros pares ingresados.
#Suma de numeros positivos.
#Promedio de los numeros impares ingresados.

from os import system
system("cls")

i=1
suma=0
contpar=0
contimpar=0
sumaimpar=0
while(True):
    while(True):
        try:
            cantnum=int(input("Ingrese un numero entero positivo: "))
            if(cantnum>0):
                suma+=cantnum
                if(cantnum%2==0):
                    contpar+=1
                else:
                    contimpar+=1
                    sumaimpar+=cantnum
                break
            elif(cantnum==0):
                print("No se puede trabajar con 0 numeros.")
                continue
            else:
                print("No se adminten numeros negativos.")
                continue
        except ValueError:
            print("Necesita ingresar un numero entero para poder trabajar, no se admiten ni decimales ni caracteres.")
            continue
    while(True):
        try:        
            pregunta=input("Desea ingresar otro numero? (S=si / N=no): ").upper()
            if(pregunta=="S"):
                while(True):
                    try:
                        cantnum2=int(input("Ingrese un numero entero positivo: "))
                        if(cantnum2>0):
                            suma+=cantnum2
                            if(cantnum2%2==0):
                                contpar+=1
                            else:
                                contimpar+=1
                                sumaimpar+=cantnum2
                            break
                        elif(cantnum2==0):
                            print("No se puede trabajar con 0 numeros.")
                            continue
                        else:
                            print("No se adminten numeros negativos.")
                            continue
                    except ValueError:
                        print("Necesita ingresar un numero entero para poder trabajar, no se admiten ni decimales ni caracteres.")
                    continue
            elif(pregunta=="N"):
                break
            else:
                print("Solo se admiten los caracteres de 'S' o 'N'")
                continue
        except ValueError:
            print("Solo se admiten los caracteres de 'S' o 'N'")
            continue
    break
promedio=sumaimpar/contimpar
print("La cantidad de numeros pares ingresados es: {}".format(contpar))
print("La suma de los numeros positivos da como resultado: {}".format(suma))
print("El promedio de los numeros pares ingresados es: {}".format(promedio))