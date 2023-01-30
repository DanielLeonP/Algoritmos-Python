from time import time
def Gnome_sort(vector):
    i_b,i_i,taille = 1,2,len(vector)
    while i_b < taille:
        if vector[i_b-1] <= vector[i_b]:
            i_b,i_i = i_i, i_i+1
            
        else:
            vector[i_b-1],vector[i_b] = vector[i_b],vector[i_b-1]
            i_b -= 1
            
            if i_b == 0:
                i_b,i_i = i_i, i_i+1
        print(vector)
    return vector

vector = [29,222,3,9,543,18,10,5,4,22,1,33,999,21,456,200,7,2,887,6]
t0 = time()
Gnome_sort(vector)
t1 = time()
print(vector)
print("Tiempo: {0:f} segundos".format(t1-t0))