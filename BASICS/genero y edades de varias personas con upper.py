#Ejercicio en clases python 1
#Upper transforma a mayuscula y lower a minusculas
edad1=int (input("Ingrese la edad de la primera persona"))
gen1=input("Ingrese el genero del la primera persona (F:femenino/M:masculino)").upper()
edad2=int (input("Ingrese la edad de la segunda persona"))
gen2=input("Ingrese el genero del la segunda persona (F:femenino/M:masculino)").upper()
edad3=int (input("Ingrese la edad de la tercera persona"))
gen3=input("Ingrese el genero del la tercera persona (F:femenino/M:masculino)").upper()
edad4=int (input("Ingrese la edad de la cuarta persona"))
gen4=input("Ingrese el genero del la cuarta persona (F:femenino/M:masculino)").upper()
edad5=int (input("Ingrese la edad de la quinta persona"))
gen5=input("Ingrese el genero del la quinta persona (F:femenino/M:masculino)").upper()

contMujer=0 #Aqui se cuentan las mujeres
contHombre=0 #Aqui se cuentan los hombres

if (gen1=="F"):
    contMujer+=1
else:
    contHombre+=1
if (gen2=="F"):
    contMujer+=1
else:
    contHombre+=1
if (gen3=="F"):
    contMujer+=1
else:
    contHombre+=1
if (gen4=="F"):
    contMujer+=1
else:
    contHombre+=1
if (gen5=="F"):
    contMujer+=1
else:
    contHombre+=1
print ("El total de mujeres es : ",contMujer)
print ("El  total de hombres es :",contHombre)                                    