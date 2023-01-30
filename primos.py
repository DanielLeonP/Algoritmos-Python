

def primo(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True      
def posicion(lista, llave):
    cantidadPrimos = 0 
    for i in range(0, len(lista)):              
        if (lista[i] == llave):
            print("El número se encuentra en la posición ", i+1) 
            print("La cantidad de números primos encontrados en la lista y menores que ", llave, "es ", cantidadPrimos)
            return           
        else:
            if(primo(lista[i])):
              cantidadPrimos = cantidadPrimos + 1        
        
lista = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
llave = int(input("Número a buscar:"))
posicion(lista, llave)

  