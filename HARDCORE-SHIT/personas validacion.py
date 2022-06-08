#Ingresar la edad y genero ([M]: Masculino, [F]: Femenino) de N personas y luego mostrar:
#Promedio de las edades.
#Promedio de las edades de los hombres.
#Cantidad de mujeres con edad mayor a 30 años.
#Mayor edad ingresada.

from os import system
system("cls")

person=1
sumaedad=0
edadhombres=0
conthombres=0
mujerm30=0
lista=[]

while(True):
    person+=1
    while(True):
        try:
            edad=int(input("Ingrese la edad de la persona: "))
            if(edad>0):
                lista.append(edad)
                sumaedad+=edad
                break
            elif(edad==0):
                print("La edad no puede ser 0.")
            else:
                print("La edad no puede ser un numero negativo.")
        except ValueError:
            print("No se admiten numeros decimales y/o caracteres.")
    while(True):
        try:
            gen=input("Ingrese el genero de la persona ([M]: Masculino, [F]: Femenino): ").upper()
            if(gen=="M") or (gen=="F"):
                if(gen=="M"):
                    conthombres+=1
                    edadhombres+=edad
                if (gen=="F") and (edad>30):
                    mujerm30+=1
                break
            else:
                print("Solo se admiten los caracteres 'M' o 'F'")
        except ValueError:
            print("Solo se admiten los caracteres 'M' o 'F'")
    while(True):
        try:
            pregunta=input("Desea ingresar a otra persona? ([S]:si [N]:no): ").upper()
            if(pregunta=="S"):
                person+=1
                while(True):
                    try:
                        edad=int(input("Ingrese la edad de la persona: "))
                        if(edad>0):
                            lista.append(edad)
                            sumaedad+=edad
                            break
                        elif(edad==0):
                            print("La edad no puede ser 0.")
                        else:
                            print("La edad no puede ser un numero negativo.")
                    except ValueError:
                        print("No se admiten numeros decimales y/o caracteres.")
                while(True):
                    try:
                        gen=input("Ingrese el genero de la persona ([M]: Masculino, [F]: Femenino): ").upper()
                        if(gen=="M") or (gen=="F"):
                            if(gen=="M"):
                                conthombres+=1
                                edadhombres+=edad
                            if (gen=="F") and (edad>30):
                                mujerm30+=1
                            break
                        else:
                            print("Solo se admiten los caracteres 'M' o 'F'")
                    except ValueError:
                        print("Solo se admiten los caracteres 'M' o 'F'")
            elif(pregunta=="N"):
                break
            else:
                print("Solo se admiten los caracters 'S' y 'N'")
                continue
        except ValueError:
            print("Solo se admiten los caracters 'S' y 'N'")
    break
promedioedad=(sumaedad/person)
promedioedadhombres=(edadhombres/conthombres)
edadmayor=max(lista)

print("Lista de edades: {}".format(lista))
print("Promedio de edades: {}".format(promedioedad))
print("Promedio de edades de hombres: {}".format(promedioedadhombres))
print("La cantidad de mujeres mayores de 30 años es: {}".format(mujerm30))
print("La edad mayor ingresada fue: {}".format(edadmayor))