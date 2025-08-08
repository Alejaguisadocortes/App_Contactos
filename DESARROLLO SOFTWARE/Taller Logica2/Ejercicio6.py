#Verificación de número primo:
# Usa un ciclo for para verificar si un número es divisible 
# por algún número entre 2 y su raíz cuadrada.
# Si no tiene divisores, es primo.

numero = 11
es_primo = True

for i in range(2, numero):
    if numero % i == 0:
        es_primo = False
        break
if es_primo:
    print("El numero", numero, "es primo") 
else: 
   print("El numero", numero, "no es primo")  
   
