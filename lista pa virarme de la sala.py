listaA=["Berserk", "Death Note", "Dr.Stone", "Dragon ball Z", "Steins Gate"]
listaG=[]
for i in listaA:
    print("Mono chino: {}".format(i))
    Genero=input("Ingrese la demografia del mono chino de la lista: ")
    listaG.append(Genero)
for i in range(len(listaA)):
    print("La demografia del mono chino " + listaA[i] + " corresponde a " + listaG[i])