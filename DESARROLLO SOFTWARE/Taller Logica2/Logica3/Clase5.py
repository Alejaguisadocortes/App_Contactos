arreglo = []
numero = len(arreglo)

#para que o que?
#Rehusar codigo
#DRY: No repetir a ti mismo el codigo (Don´t
#repeat yourself).
#KISS: Keep it simple, stupid.
# #En lugar de escribir el codigo varias veces,
# escribo una sola vez en una funcion y la llamo
# cuando necesite.

# Organizacion y modular.
# dividir un programa en funciones hace
# que el codigo sea mas estructurado y facil de
# entender.


#Facilidad del mantenimiento.
#si hay errores en la ejecucion se pueden corregir en una sola funcion, en lugar
#de buscar en varias partes del programa.


#Escalabilidad. 
#se puede agrandar el alcance que se le da al proyecto en menos lineas de 
#codigo. construir programas mas grandes de una manera mas ordenada y logica.

#Facilitan el trabajo en equipo sin afectar otras partes del codigo.classmethod


#componentes de una funcion.

#Nombre de la funcion: Identificador unico que permite llamarla cuando sea 
#necesario.
#Ej. (.ordenar)

#parametros(opcional):
#datos que reciben una funcion para trabajar con ellos.

#Cuerpo de la funcion:
#bloque de codigo que define el comportamiento de la funcion.

#valor de retorno(opcional): Resultado que la funcion va a devolver al flujo
#principal.

#diferencia entre una funcion y un bloque de codigo.

print("Hola bienvenido a nuestro programa")
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}, espero que tengas un buen dia!")

print("Hola bienvenido a nuestro programa")
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}, espero que tengas un buen dia!")

#Aqui no hay defindas funciones sino bloque de codigo.

#/////////////////////////////////////
#Ejemplo en pseudocodigo de como calcular el area de un rectangulo

#1 pedir la base y la altura
#2 multiplicar base*altura
#3 mostrar el resultado.

#parametros y retornos:
#las funciones reciben parametros que devuelven resultados.

#parametro es: el insumo con el que trabaja la funcion.

#retorno: es el resultado de procesar los parametros.

#1 ingresar "late" y "grande" como parametros a la maquina.
#2 la maquina prepara el cafe.
#3 la maquina devuelve el cafe listo.
