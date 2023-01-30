def particion(lista, izq, der): #partición
    global comparaciones
    pivote = lista[der]
    indice = izq
    comparaciones = 0

    for i in range(izq, der):
        comparaciones = comparaciones + 1
        if lista[i] <= pivote:
            lista[indice], lista[i] = lista[i], lista[indice]
            indice = indice + 1
    lista[indice], lista[der] = lista[der], lista[indice]
    return(indice)

def quicksort(lista, izq, der): #orden
    if izq < der:
        pivote_indice = particion(lista, izq, der)
        quicksort(lista, izq, pivote_indice - 1)
        print("El pivote esta en la posición:", pivote_indice)
        quicksort(lista, pivote_indice + 1, der)

lista = [5, 26, 9, 15, 23, 17, 13, 7]
print(lista)
quicksort(lista, 0, len(lista) - 1)
print("Comparaciones:", comparaciones)
print("Lista Ordenada:", lista)