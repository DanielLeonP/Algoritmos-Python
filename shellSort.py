from time import time

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
      for start_position in range(sublistcount):
        gap_InsertionSort(alist, start_position, sublistcount)
      print("Despues de incrementar el tamaño de la distancia a",sublistcount, "La lista es",nlist)
      sublistcount = sublistcount // 2

def gap_InsertionSort(nlist,start,gap):
    for i in range(start+gap,len(nlist),gap):
        current_value = nlist[i]
        position = i
        while position>=gap and nlist[position-gap]>current_value:
            nlist[position]=nlist[position-gap]
            position = position-gap
        nlist[position]=current_value

nlist = [29,222,3,9,543,18,10,5,4,22,1,33,999,21,456,200,7,2,887,6]
t0 = time()
shellSort(nlist)
t1 = time()
print(nlist)
print("Tiempo: {0:f} segundos".format(t1-t0))