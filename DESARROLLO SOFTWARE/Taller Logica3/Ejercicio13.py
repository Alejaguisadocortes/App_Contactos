# 13. Lista de números aleatorios: Genera una lista de 20 números aleatorios y 
# ordénalos con el algoritmo de mergesort.

def merge(lista1, lista2):
    
    lista3= []
    
    while(len(lista1) > 0 and len(lista2) > 0):
        if lista1[0] < lista2[0]:
            lista3.append(lista1[0])
            lista1 = lista1[1:]
        
        else:
            lista3.append(lista2[0])
            lista2 = lista2[1:]
        
    if len(lista1) > 0:
        lista3 = lista3 + lista1
    if len(lista2) > 0:
        lista3 = lista3 + lista2
    return lista3
            

def mergesort(lista):
    if len(lista) == 1:
        return lista
    
    lista1 = lista[:len(lista)//2]
    lista2 = lista[len(lista)//2:]

    lista1 = mergesort(lista1)
    lista2 = mergesort(lista2)
    
    return merge(lista1, lista2)
        
    

lista = [78, 15, 22, 56, 90, 68, 2, 8, 79, 45, 10, 47, 13, 71, 27, 4, 25, 
         33, 55, 66]
print(lista)
print(mergesort(lista))