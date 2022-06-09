from os import system
system("cls")

listaA=["Berserk", "Death Note", "Dr.Stone", "Dragon ball Z", "Steins Gate"]
listaG=[]

for i in listaA:
    while(True):
        print("Mono chino: {}".format(i))
        print("")
        try:
            Genero=input("Ingrese la demografia del mono chino de la lista: ")
            if(Genero=="Seinen") or (Genero=="Shonen"):
                listaG.append(Genero)
                break
            else:
                print("")
                print("Error, debe ingresar una demografia valida (Shonen/Seinen)")
                continue
        except ValueError:
            print("")
            print("Error, debe ingresar una demografia valida (Shonen/Seinen)")
            continue

print("")
for i in range(len(listaA)):
    print("La demografia del mono chino " + listaA[i] + " corresponde a " + listaG[i])
print("")