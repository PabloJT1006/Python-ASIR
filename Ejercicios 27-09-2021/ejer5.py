import math
#Un programa en el cual introduzcamos los tres términos independientes a,b, c de una ecuación de segundo grado. calcular x1 y x2. ¿ Es posible controlar si dicha ecuación de segundo grado tiene valores complejos o no?
print("Introduce los tres valores de una ecuacion de 2º grado para calcular si el resultado seria positivo o negativo")
a=float(input("A: "))
b=float(input("B: "))
c=float(input("C: "))

complejo=b**2-(4*a*c)
if complejo>=0:
    print("El resultado seria un numero real")
else:
    print("El resultado seria un numero complejo")


#ecuacion1=(-b+math.sqrt(complejo))/2
#ecuacion2=(+b+math.sqrt(complejo))/2

#if complejo>=0:
   # print("Los resultados de la ecuacion serian: ",ecuacion1," y ",ecuacion2)
#if complejo<0:
    #print("Los resultados de la ecuacion serian: ",ecuacion1,"i y ",ecuacion2,"i")


