#Factorial de un número dado:
# Encuentra el factorial de un número multiplicando todos los números desde 1 hasta
# ese número con un ciclo for. Asegúrate de inicializar la variable acumuladora en 1.

factorial = 1

for numero in range(1, 20):
    factorial *= numero
print(f"El factorial del numero es: {factorial}")