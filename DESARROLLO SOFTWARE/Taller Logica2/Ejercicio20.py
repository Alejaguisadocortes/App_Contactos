#Promedio ponderado: Calcula el promedio ponderado de una
#lista de calificaciones. Multiplica cada calificación por su 
#peso en un ciclo for y divide entre el total de pesos.

calificaciones = [3.3, 3.5, 3.8, 4.2, 4.8]
ponderado = 0

for i in calificaciones: 
    ponderado += i
    valor = ponderado / len(calificaciones)
print(calificaciones)
print(f"El promedio ponderado de las calificaciones es: ", valor)
