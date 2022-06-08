asignaturas=["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas=[]
for i in asignaturas:
    nota=input("¿Qué nota has sacado en " + i + "? ")
    notas.append(nota)
for i in range(len(asignaturas)):
    print("En " + asignaturas[i] + " has sacado " + notas[i])