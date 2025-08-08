#Encuentra el MCD de dos numeros, utilizando
#el algoritmo de euclides con un ciclo while, que repite
#el calculo del residuo hasta que uno de los dos numeros sea cero.

def MCD(a, b): 
 if b>a:a, b=b,a  
 while a % b!=0:  
  b,a = a%b, b  
 return b  
x=360
y=3876
print('El MCD de {} y {} es {}.'.format(x,y,MCD(x,y)))