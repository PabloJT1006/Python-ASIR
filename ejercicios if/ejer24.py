#24. Programa que calcule el factorial de un número introducido por teclado, sabiendo que la 
# fórmula del factorial el factorial (n) = n * factorial (n-1).
numero=float(input("Introduce un numero para calcular su factorial: "))
factorial=1
while numero>1:
    factorial*=numero
    numero-=1
    

print("El factorial del numero introducido es: ",factorial)