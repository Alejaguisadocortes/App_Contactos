#Recorre cada elemento de una lista con un ciclo for,
#acumula su suma y divide entre el numero total de elementos
#para calcular la media.
numeros = [1,2, 3, 4, 5]
suma = 0

for numero in numeros:
    suma += numero
    print(f"La media es", suma)
    