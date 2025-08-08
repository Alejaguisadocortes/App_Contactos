# 9. Ordenación de ventas diarias: Se registraron ventas diarias de una tienda. 
# Ordénalas en orden ascendente con inserción.

Ventas_Diarias = [200.980, 980.456, 327.975, 541.009, 128.657]
n = len(Ventas_Diarias)

for i in range(1, n):
    Orden = Ventas_Diarias[i]
    j = i -1
    while j >= 0 and Ventas_Diarias[j] > Orden:
        Ventas_Diarias[j + 1] = Ventas_Diarias[j]
        j -= 1
    Ventas_Diarias[j + 1] = Orden

print(f"El orden de las ventas por monto es: {Ventas_Diarias}")