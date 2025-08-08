#Área de un triángulo: Calcula el área de un triángulo 
#dada su base y altura con la fórmula (base * altura) / 2. 
#Este ejercicio no requiere un ciclo for.

base = int(input("Ingrese la base del triangulo"))
altura = int(input("Ingrese la altura del triangulo"))

area = (base * altura)/ 2

print(f"El area del triangulo es: " + str(area))