#insercion
from time import time
def ord_insercion(list2a):
    for i in range(len(lista2)-1):
        if lista2[i+1] < lista2[i]:
            reubicar(lista2, i+1)
        print(lista2)

def reubicar(lista2, posicion):
    v = lista2[posicion]
    j = posicion
    while j > 0 and v < lista2[j-1]:
        lista2[j] = lista2[j-1]
        j-=1
        lista2[j] = v


lista2 = [29,222,3,9,543,18,10,5,4,22,1,33,999,21,456,200,7,2,887,6]

print("Lista original= ", lista2)
t0 = time()
ord_insercion(lista2)
t1= time()
print("Tiempo: {0:f} segundos".format(t1-t0))