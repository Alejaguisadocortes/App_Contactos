#sin funciones

productos = []
precios = []

for i in range_(3):
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input(f"Ingrese el precio de {nombre}: "))
    productos.append(nombre)
    precios.append(precio)
    
total = 0
for precio in precio:
    total += precio
    
if total > 100: 
    total = total *0.90
    
print("\nResumen de compra:")
for i in range(len(productos)):
    print(f"{productos[i]} - ")