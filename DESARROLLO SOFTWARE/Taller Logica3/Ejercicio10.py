# 10. Ordenación de distancia entre ciudades: Dado un arreglo con distancias 
# entre ciudades, ordénalas de menor a mayor usando inserción.

Distancias = [33.34, 12.54, 15.92, 25.88, 67.13]
n = len(Distancias)

for i in range(1, n):
    Ciudad = Distancias[i]
    j = i -1
    while j >= 0 and Distancias[j] > Ciudad:
        Distancias[j + 1] = Distancias[j]
        j -= 1
    Distancias[j + 1] = Ciudad

print(f"El orden de las distancias es: {Distancias}")