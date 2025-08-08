# 11. Ordenación de salarios: Dado un conjunto de salarios de empleados, 
# ordénalos utilizando el método de selección.

Salarios = [3500450, 4852500, 1456200, 3221890, 7345600]
Seleccion = len(Salarios)

for i in range(Seleccion-1):
    print(Salarios)
    menor = i
    print("El indice actual para comparar es: ", menor)
    for j in range(i+1, Seleccion):
        if Salarios[j] < Salarios[menor]:
           menor = j
           print("Recorriendo los salarios", menor)           
                  
    temporal = Salarios[menor]
    Salarios[menor] = Salarios[i]
    Salarios[i] = temporal
    print("Cambiamos el elemento", Salarios[menor], "por el elemento",
          Salarios[i])