#Cantidad de vocales en una cadena: Recorre cada carácter de una 
#cadena de texto con un ciclo for y cuenta cuántos de ellos son vocales.

def contar_vocales(cadena):
    contador = 0
    for vocal in cadena:
        if vocal.lower() in "aeiou":
            contador += 1
    return contador

cadena = "Hoy vamos a revisar si si la cogieron. Hola mundo"
cantidad = contar_vocales(cadena)

print(cadena)
print(F"En la cadena '{cadena}' hay {cantidad} de vocales: ")       