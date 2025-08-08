# 1. Ordenación de notas de estudiantes: Dado un 
# arreglo de calificaciones, ordénalas de menor 
# a mayor usando el método de burbuja.

calificaciones = [20, 98, 55, 13, 77]

for i in range(len(calificaciones) -1):
    for j in range(len(calificaciones) -1):
        if calificaciones[j] > calificaciones[j+1]:
            
           temporal = calificaciones[j]
           calificaciones[j] = calificaciones[j+1]
           calificaciones[j+1] = temporal

print(calificaciones)



