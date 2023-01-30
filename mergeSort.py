#Agrega un vector aleatorio
#import numpy as np
#Algoritmo metodo por ordenamiento por mezcla(mergeSort)
from time import time
def mergeSort(alista):
    print("Divide", alista)
    if len(alista)>1:
        mitad = len(alista)//2
        ladoIzquierdo = alista[:mitad]
        ladoDerecho = alista[mitad:]
        mergeSort(ladoIzquierdo)
        mergeSort(ladoDerecho)
        i = 0
        j=0
        k=0
        while (i < len(ladoIzquierdo) and j<len(ladoDerecho)):
            if (ladoIzquierdo[i]< ladoDerecho[j]):
                alista[k]= ladoIzquierdo[i]
                i = i+1
            else:
                alista[k] = ladoDerecho[j]
                j = j+1
            k = k+1
        while(i< len(ladoIzquierdo)):
            alista[k] = ladoIzquierdo[i]
            i = i+1
            k = k+1
        while(j < len(ladoDerecho)):
            alista[k] = ladoDerecho[j]
            j = j+1
            k= k+1
        print("Mezclando", alista)

alista = [29,222,3,9,543,18,10,5,4,22,1,33,999,21,456,200,7,2,887,6]  #np.random.randint(1000, size=1000)

t0 = time()
mergeSort(alista)
t1 = time()
print(alista)
print("Tiempo: {0:f} segundos".format(t1-t0))