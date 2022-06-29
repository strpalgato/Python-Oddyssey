import numpy as np
camarote=0
while(True): # creacion de matriz
    matriz=np.empty((6,6))
    for i in range(6):
        for j in range(6):
            while(True):
                camarote+=1
                break
            matriz[i,j]=camarote
    break
print(matriz)
matrizlen=len(matriz)
print(matrizlen)