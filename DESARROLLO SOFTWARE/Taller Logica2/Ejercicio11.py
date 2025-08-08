#Invertir un número: Recorre los dígitos de un número desde el 
#principio hasta el final utilizando un ciclo for 
#y constrúyelo en orden inverso.

num = int(input("Ingrese el numero: "))
resultado = " "

for char in str(num) [:: -1]:
    resultado += char
print(resultado)
    
      