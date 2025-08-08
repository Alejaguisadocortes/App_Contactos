# 3. Temperaturas diarias: Un sensor registra las temperaturas de una semana. 
# Ordena los valores de mayor a menor utilizando burbuja.


temperaturas = [34.5, 45.3, 33, 38, 36]
n = len(temperaturas)

for i in range(len(temperaturas) -1):
    for j in range(len(temperaturas) -1):
        if temperaturas[j] < temperaturas[j+1]:
            
           temporal = temperaturas[j]
           temperaturas[j] = temperaturas[j+1]
           temperaturas[j+1] = temporal

print(f"Las temperaturas mayor a menor: {temperaturas}")


   