from os import system
system("cls")

import random
sumanota=0
contpar=0
contimpar=0
listapromedio=[]
listadecimas=[]

while(True):
    print("Lista de promedios {}".format(listapromedio))
    print("Lista de decimas {}".format(listadecimas))
    while(True):
        try:
            cantnotas=int(input("Ingrese la cantidad de notas con las que desea trabajar: "))
            if (cantnotas>0) and (cantnotas<10):
                break
            else:
                print("La cantidad de notas ingresada no es válida.")
                continue
        except ValueError:
            print("Solo se admiten numeros enteros positivos.")
            continue
    if(cantnotas==9):
        break
    i=1
    while(i<=cantnotas):
        print("Nota #{}".format(i))
        while(True):
            try:
                nota=float(input("Ingrese la nota: "))
                if(nota==9):
                    i+=cantnotas
                    break
                elif(nota>=1) and (nota<=7):
                    sumanota+=nota
                    break
                else:
                    print("La nota ingresada no es válida.")
                    continue
            except ValueError:
                print("La nota ingresada no es válida. (Solo se admiten números decimales positivos)")
                continue
        i+=1
    if(nota==9):
        break

    promedio=(sumanota/cantnotas)
    promedioredon=round(promedio, 1)
    print("")
    print("El promedio de este alumno es: {}".format(promedioredon))
    listapromedio.append(promedioredon)

    promedioredon=promedioredon*10
    alrevez=0
    while(promedioredon!=0):
        b=promedioredon%10 #rescato el ultimo digito
        if(b%2==0):
            contpar+=1 #El ultimo digito es par
        else:
            contimpar+=1 #El ultimo digito es impar
        alrevez=(alrevez*10) + b
        promedioredon=promedioredon//10 #division entera, para achicar el numero
    alrevez=alrevez/10
    print("La cantidad de numeros pares que posee el promedio es: {}".format(contpar))
    print("La cantidad de numeros impares que posee el promedio es: {}".format(contimpar))
    print("El promedio invertido de este alumno es: {}".format(alrevez))

    while(True):
        print("")
        print("¿Este alumno se encuentra 'APROBADO' o 'REPROBADO'?: ")
        try:
            pregunta=input().upper()
            if (pregunta=="APROBADO"):
                break
            elif(pregunta=="REPROBADO"):
                break
            elif(pregunta=="9"):
                break
            else:
                print("La respuesta ingresada no es válida. (Solo se admite 'APROBADO' o 'REPROBADO')")
        except ValueError:
            print("La respuesta ingresada no es válida. (Solo se admite 'APROBADO' o 'REPROBADO')")
    if(pregunta=="9"):
        break
    if(pregunta=="APROBADO"):
        curso=random.randint(0,1)
        print("")
        if curso==0:
            print("Este alumno será asignado al curso A")
        elif curso==1:
            print("Este alumno será asignado al curso B")

        decimas=(random.random())
        decimasredon=round(decimas, 1)
        listadecimas.append(decimasredon)

        if decimasredon==0:
            print("Este alumno no obtuvo decimas")
        else:
            print("Este alumno obtuvo {} decimas".format(decimasredon))

    while(True):
        print("¿Desea ingresar otro alumno? (S=si / N=no)")
        try:
            respuesta=input().upper()
            if(respuesta=="S"):
                break
            elif(respuesta=="N"):
                print("")
                print("Programa finalizado exitosamente.")
            else:
                print("Los carácteres ingresados no son válidos. (Solo se admite 'S' o 'N')")
        except ValueError:
            continue
    promedio=0
    sumanota=0
    contpar=0
    contimpar=0
    continue
print("Datos guardados, vuelva pronto.")