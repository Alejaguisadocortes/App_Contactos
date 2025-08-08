#Suma de los dígitos de un número con ciclos: Extrae cada dígito
#de un número utilizando operaciones matemáticas y acumula su 
#suma dentro de un ciclo.

def suma_digitos(numero):
    suma = 0
    while numero > 0:
        digito = numero % 10
        suma += digito
        numero = numero // 10
    return suma 

numero = int(input("Ingresa un numero entero: "))
resultado= suma_digitos(numero)

print(f"La suma de los digitos de {numero} es: {resultado} ")