#Suma de los primeros n números naturales:
#Calcula la suma de los números desde 1 hasta n utilizando un ciclo for.
#Itera sobre los números en el rango de 1 a n y acumula su suma.
suma = 0

for numero in range(1, 11):
    suma += numero
print(f"La suma de los numeros naturales del 1 al 11 es:", {suma})