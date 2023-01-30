def busquedaSecuencial(lista,llave):
    posicion=0
    encontrado=False
    while posicion<len(lista)and not encontrado:
        if lista[posicion] == llave:
            encontrado=True
        else:
            posicion= posicion+1
    return encontrado, posicion

lista= [29,222,3,9,543,18,10,5,4,22,1,33,999,21,456,200,7,2,887,6]
llave = int(input("¿Cual es la llave que quuieres buscar?"))

print("lista", lista)
print(busquedaSecuencial(lista,llave))



#ALgoritmo de busqueda binaria