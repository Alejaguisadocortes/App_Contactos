#Mínimo común múltiplo (LCM):
# Calcula el MCM de dos números utilizando el MCD
# previamente obtenido y el producto de ambos.

a, b = 3, 5
original_a, original_b = a, b

while b:
    a, b = b, a % b
mcd = a
lcm = abs(original_a * original_b) // mcd

print("LCM:", lcm)