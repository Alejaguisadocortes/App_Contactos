# 4. Orden de llegada de corredores: Dado un listado de tiempos de llegada 
# en una carrera, ordénalos de menor a mayor usando burbuja.

Tiempos = [ 45, 36, 29, 57, 20 ]

for i in range(len(Tiempos) -1):
    for j in range(len(Tiempos) -1):
        if Tiempos[j] > Tiempos[j+1]:
            
           temporal = Tiempos[j]
           Tiempos[j] = Tiempos[j+1]
           Tiempos[j+1] = temporal

print(Tiempos)

