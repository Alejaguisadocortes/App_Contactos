#Número más grande en una lista: Compara los números 
#de una lista uno por uno utilizando un ciclo for 
#para encontrar el mayor de ellos.

lista = [1, 2, 3, 4, 5]
alto = lista[0]
for i in range(0, len(lista)):
    if lista[i]> alto:
        alto = lista[i]
print(lista)
print(f"El numero mayor es: ", alto)       

