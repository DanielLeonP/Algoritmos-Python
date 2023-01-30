""" def ord_insercion(lista):
    for i in range(len(lista)-1):
        if lista[i+1] < lista[i]:
            reubicar(lista, i+1)
        return lista
def reubicar(lista, posicion):
    v = lista[posicion]
    j = posicion
    while j > 0 and v < lista[j-1]:
        lista2[j] = lista[j-1]
        j-=1
        lista2[j] = v
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
    lista = ord_insercion(lista)
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
posicion(lista, llave) """


seed_number = int(input("Please enter a four digit number:\n[####] ")) 
number = seed_number 
already_seen = set() 
counter = 0 
while number not in already_seen: 
    counter += 1 already_seen.add(number) 
    number = int(str(number * number).zfill(8)[2:6])
 # zfill adds padding of zeroes print(f"#{counter}: {number}") print(f"We began with {seed_number}, and" f" have repeated ourselves after {counter} steps" f" with {number}.") Método del cuadrado medio - https://es.qaz.wiki/wiki/Middle-square_method