# 8. Ordenación de caracteres en una palabra: Dada una palabra, ordénala 
# alfabéticamente utilizando el método de inserción.

Palabra = input("Ingrese 1 palabra: ").split()

for i in range(1, len(Palabra)):
    Orden = Palabra[i]
    j = i - 1
    while j >= 0 and Orden < Palabra[j]:
        Palabra[j+1] = Palabra[j]
        j -= 1
    Palabra[j+1] = Orden

print(f"palabra ordenada alfabeticamente: {Palabra}. ")