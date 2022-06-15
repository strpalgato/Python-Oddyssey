from multiprocessing.sharedctypes import Value
import numpy as np

sw=0
while(sw==0):

    while(True):
        try:
            n=int(input("Ingrese largo de las filas de la matriz: "))
            if(n>0):
                break
            else:
                print("Debe ser un numero positivo")
        except ValueError:
            print("Debe ser numero entero")
    while(True):
        try:
            m=int(input("Ingrese largo de la columna de la matriz (debe ser diferente al largo de las filas): "))
            if(m>0):
                break
            else:
                print("Debe ser un número positivo")
        except ValueError:
            print("Debe ser un número entero")
    if(m!=n):
        sw=1
    else:
        print("El valor de las filas debe ser distinto al de las columnas")



matriz=np.empty((n,m)) #defino una matriz de n por n

for i in range(n):
    for j in range (m):
        while(True):
            try:
                num=int(input("Ingrese un numero: "))
                break
            except ValueError:
                print("Debe ser un numero entero")
        matriz[i,j]=num #matriz [i][j]=num

for i in range(n):
    for j in range(m):
        print(matriz[i,j])
    print()
print(matriz)