# 6. Ordenación de edades: Un grupo de personas tiene diferentes edades. Utiliza 
# inserción para ordenarlas de menor a mayor.

Edades = [45, 66, 29, 12, 70]
n = len(Edades)

for i in range(1, n):
    Grupo = Edades[i]
    j = i -1
    while j >= 0 and Edades[j] > Grupo:
        Edades[j + 1] = Edades[j]
        j -= 1
    Edades[j + 1] = Grupo

print(f"Las edades con insercion : {Edades}")