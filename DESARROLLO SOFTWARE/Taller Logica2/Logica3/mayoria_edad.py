#sin funciones

edad = int(input("Ingrese su edad"))

if edad >= 18:
 print("Eres mayor de edad")
else:
     print("Te redirijo a Google.")

#con funciones
def verificar_edad(edad):
   if edad >= 18:
    print("Eres mayor de edad")
   else:
       print("Te redirijo a Google.")

edad_usuario = int(input("Ingrese su edad: "))
verificar_edad(edad_usuario)