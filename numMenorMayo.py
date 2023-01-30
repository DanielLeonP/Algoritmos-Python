#Seleccion
#Insercccion
#mergeSort
#quicksort

""" 
#Ordenamiento, por la maestra , no funciona
from time import time
def ordenSeleccion(lista):
    n = len(lista)-1
    while n>0:
        p = buscarMaximo(lista,0,n)
        lista[p], lista[n] = lista[n],lista[p]
        print ("DEBUG:", p, n, lista)
        n = n-1
def buscarMaximo(lista, ini, fin):
    posicionMaxima = ini
    for i in range(ini + 1,fin + 1):
        if(lista[i]>lista[posicionMaxima]):
            posicionMaxima = i
        return posicionMaxima

lista = [3,9,18,10,5,4,22,1,33,1,21]
print("Lista original= ", lista)
t0 = time()
ordenSeleccion(lista)
t1= time()
print("Tiempo: {0:f} segundos".format(t1-t0)) """






"""#ordenar mio
arreglo = [7,10,53,2,4,9]
for j in range(len(arreglo)):
    for i in range(len(arreglo)-1):
        if arreglo[i] > arreglo[i+1]:
            temporal = arreglo[i]
            arreglo[i] = arreglo[i+1]
            arreglo[i+1] = temporal
            print(arreglo)
print("El arreglo ordenado de menor a mayor es ", arreglo) """





""" 
#Ordenar con .sort
from time import time
lista = [3, 9, 18, 10, 5, 4, 22, 1, 21]
t0 = time()
lista.sort()
print(lista)
t1 = time()
print("Tiempo: {0:f} segundos".format(t1-t0)) """




""" def calcularSuma(n):
  if n>0:
    n = n + calcularSuma(n - 1)
  return n
print ("El resultado de la suma es ",calcularSuma(9))
 """




""" #Respuestapregunta Por medio de un ciclo for (int i =9; i>0, i--) {acumulador = acumulador + i}, el resultado de la suma será el acumulador. Otra manera de realizarlo sería por medio de una función calcularSuma(n){if (n>0){ n = n + calcularSuma(n - 1)} return n }, donde el resultado de la suma = calcularSuma(9). """

""" 
#alg maestra por seleccion
def OrdenaS(lista):
    n = len(lista) - 1
    print(n)
    for i in range(0,n+1):
        for j in range(i+1, n+1):
            pivote = lista[i]
            #print("DEBUG pivote ", pivote)
            #print("DEBUG lista[j]", lista[j])
            if(pivote > lista[j]):
                auxiliar = pivote
                lista[i] = lista[j]
                lista[j] = pivote
            
lista = [3,9,18,4,10, 5,1,22,21]
print("lista original= ", lista)
OrdenaS(lista)
print("lista final = ", lista) """



""" #Funciono
#Algoritmo ordenamiento por inserccion
from time import time
def ordenar(arreglo):
    for j in  range(len(arreglo)):
        llave = arreglo[j]
        i=j-1        
        while(i>-1 and arreglo[i]>llave):            
            arreglo[i+1] = arreglo[i]
            i = i-1
        arreglo[i+1] = llave
        print(arreglo)
arreglo = [9,3,7,4,6]
t0 = time()
ordenar(arreglo)
t1 = time()
print("Tiempo: {0:f} segundos".format(t1-t0)) """





""" 
#Algoritmo de la maestra por inserccion
def ord_insercion(list2a):
    for i in range(len(lista2)-1):
        if lista2[i+1] < lista2[i]:
            reubicar(lista2, i+1)
        print("DEBUG: ", lista2)

def reubicar(lista2, posicion):
    v = lista2[posicion]
    j = posicion
    while j > 0 and v < lista2[j-1]:
        lista2[j] = lista2[j-1]
        j-=1
        lista2[j] = v

lista2 = [3, 9, 18, 4, 10, 5, 1, 22, 21]
ord_insercion(lista2) """

 


""" #Ordenar por dividir y vencer pseudocodigo
    Función dividir(arreglo):
    if subarreglo > 1:
        arregloDerecho, arregloIzquierdo  = dividir(arregloDerecho)

    else:       
        mientras cantidadSubarreglos>2: 
            arreglo = combinar subarreglos
    return arreglo """




""" #Algoritmo mio ordenamiento por mezcla(mageSort)
from time import time
def dividir(lista,ar, acumuladorr):    
    tamanio = len(lista)
    partir= int(tamanio/2)
    if (tamanio==1):        
        ar.append(lista)
        print("Base: ", lista)
        print(ar)
        if(len(ar)==tam):
            print("Empezar a combinar....")
            combinar(ar)    
    else:
        arreglo1 = lista[0:partir]
        arreglo2 = lista[partir:tamanio]        
        print(lista,"------->",arreglo1, arreglo2)
        dividir(arreglo1, ar, tam)
        dividir(arreglo2, ar, tam)
        
def combinar(ar):
    lista = []
    acumulador = 0
    acumulador2 = 0
    if(len(ar)>1):
        for listaa in ar:
            acumulador = acumulador + 1        
            for numero in listaa:
                acumulador2 = acumulador2 + 1
                if(acumulador <= 2 ):
                    lista.append(numero)
                    ordenar(lista)   
        ar.pop(0)  
        ar.pop(0)  
        ar.append(lista)
        print("-->",ar)   
        combinar(ar)
    else:
        ordenar(ar)  
        for lista in ar:
            print("Ordenado: ", lista)   

def ordenar(arreglo):
    for j in  range(len(arreglo)):
        llave = arreglo[j]
        i=j-1        
        while(i>-1 and arreglo[i]>llave):            
            arreglo[i+1] = arreglo[i]
            i = i-1
        arreglo[i+1] = llave


t0 = time()
lista= [7,2,1,9,4,8,256,3,986,29,5]
ar = []
tam = len(lista)
dividir(lista, ar, tam)
t1 = time()
print("Tiempo: {0:f} segundos".format(t1-t0)) """




""" 
#Agrega un vector aleatorio
import numpy as np
#Algoritmo de maestra metodo por ordenamiento por mezcla(mergeSort)
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


t0 = time()
alista = np.random.randint(1000, size=1000) #[5,2,9,26,17,13,19]
mergeSort(alista)
t1 = time()
print(alista)
print("Tiempo: {0:f} segundos".format(t1-t0))
 """
