# 14. Ordenación de nombres por orden alfabético inverso: Usa el método de
# shell sort para ordenar una lista de nombres en orden descendente.
    
def shellsort(Nombres):
    n = len(Nombres)
    Orden = n // 2

    while Orden > 0:
        for i in range(Orden, n):
            temp = Nombres[i]
            j = i
            while j >= Orden and Nombres[j - Orden] < temp:
                Nombres[j] = Nombres[j - Orden]
                j -= Orden
            Nombres[j] = temp
        Orden //= 2

    return Nombres

Nombres = ["Andrea", "Ximena", "Roberto", "Beatriz", "Francia"]
nombres_ordenados = shellsort(Nombres)
print(nombres_ordenados)