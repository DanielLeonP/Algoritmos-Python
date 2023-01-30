""" def biSearch(lista, el)    
    ub = len(lista) -1
    lb = 0
    while (lb < ub-1):
        med = (ub + lb) // 2
        if lista[med] == el:
            return True
        elif lista[med] < el:
            lb = med +1
        elif lista[med] > el:
            ub = med -1
    
    return False
lista = [1,2,3,4,5]
el = int(input("Ingresa el valor:"))

print(biSearch(lista, el))

 """



def busqueda_binaria(lista, x):
    izq = 0 
    der = len(lista)-1
    while izq <= der:
        medio = (izq+der)/2
        if (lista[medio] == x):
            print(medio)
        elif (lista[medio] > x):
            der = medio-1
        else:
            izq = medio+1

lista = [1,2,3,4,5]
x = 4#int(input("¿Valor buscado?: "))
print(busqueda_binaria(lista,x))

""" repuesta = busqueda_binaria(lista,x)
if repuesta is None:
    print("El número {x} no se encontro")
else:
    print("El número {x} se encuentra en la posicion {respuesta}") """


""" def busquedaBin(vector, valor):
    derecho = len(vector) -1
    izquierdo = 0
    m=0
    while(izquierdo<= derecho):
        m=(izquierdo+derecho)/2
        if(vector[m]==valor):
            return m
        if(m<vector[valor]):
            derecho = m-1
        else:
            izquierdo = m+1
    return -1

vector = [1,2,3,4,5]
valor = int(input("¿Cuál es el valor que quuieres buscar?"))
print("vector", vector)
print(busquedaBin(vector,valor)) """