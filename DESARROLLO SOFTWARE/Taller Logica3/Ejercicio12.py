# 12. Ordenación de puntajes deportivos: Ordena una lista de puntajes deportivos 
# utilizando el método de quicksort.

def quicksort(lista):
    
    if len(lista) <= 1:
        return lista
    
    puntaje = lista.pop()
    
    lista1 =[]
    lista2 = []
    
    for i in lista:
        if i <= puntaje:
            lista1.append(i)
        else: 
            lista2.append(i)
            
    lista1 = quicksort(lista1)
    lista2 = quicksort(lista2)
    
    return lista1 + [puntaje] + lista2

lista = [33, 56, 17, 94, 75]

print(lista)
print(quicksort(lista))