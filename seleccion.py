#seleccion
#import numpy as np
from time import time
def OrdenaS(lista):
    n = len(lista) - 1
    for i in range(0,n+1):
        for j in range(i+1, n+1):
            pivote = lista[i]
          if(pivote > lista[j]):
                auxiliar = pivote
                lista[i] = lista[j]
                lista[j] = pivote
            
lista = [29,222,3,9,543,18,10,5,4,22,1,33,999,21,456,200,7,2,887,6]#np.random.randint(1000, size=1000)

print("Lista original= ", lista)
t0 = time()
OrdenaS(lista)
t1= time()
print("Lisra ordenada por seleccion:", lista)
print("Tiempo: {0:f} segundos".format(t1-t0))



