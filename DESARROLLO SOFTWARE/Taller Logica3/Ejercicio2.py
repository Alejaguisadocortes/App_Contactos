# 2. Ordenación de nombres por longitud: Ordena una lista de nombres 
# según la cantidad de caracteres utilizando ordenamiento burbuja.

nombres = ["Paula", "Juan", "Patricio", "Jorge", "Albertina"]

for i in range(len(nombres)):
    for j in range(len(nombres) -1-i):
        if (len(nombres[j]) < len(nombres[j+1])):
            estudiantes = nombres[j]
            nombres[j] = nombres[j+1]
            nombres[j+1] = estudiantes 
for i in range(len(nombres)):
    
    print(nombres[i])


 
