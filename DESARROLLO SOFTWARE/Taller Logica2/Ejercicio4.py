#Suma de los dígitos de un número:
# Recorre cada dígito de un número (convirtiéndolo en una cadena de texto) y
# suma sus valores utilizando un ciclo for.

def suma_de_digitos(numero): 
    numero = str(numero)
    suma = 0
    for i in numero:
        suma += int(i)
    return suma

numero = int(input("Digite un numero que desee que se sume sus digitos: "))

suma_2_digitos = suma_de_digitos(numero)

suma_final = int(suma_2_digitos)

print(suma_2_digitos) 