#Cantidad de dígitos de un número: Usa un ciclo for para recorrer 
#los caracteres de un número convertido a cadena de 
#texto y cuenta cuántos tiene.

number= 56743
number_string= str(number)

count= 0

for character in number_string:
    if character.isdigit():
        count+= 1

print(f"La cantidad de dígitos del número es: {count}")