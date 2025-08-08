# 5. Ordenación de precios de productos: Un sistema de inventario tiene precios 
# desordenados. Ordénalos ascendentemente con burbuja.


Inventario_Prod = [35.800, 26.500, 97.200, 13.450, 57.300]

for i in range(len(Inventario_Prod) -1):
    for j in range(len(Inventario_Prod) -1):
        if Inventario_Prod[j] > Inventario_Prod[j+1]:
            
           temporal = Inventario_Prod[j]
           Inventario_Prod[j] = Inventario_Prod[j+1]
           Inventario_Prod[j+1] = temporal

print(Inventario_Prod)