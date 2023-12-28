#16. Calcula la división de dos números introducidos utilizando restas sucesivas.
dividendo=float(input("Introduce el dividendo: "))
divisor=float(input("Introduce el divisor: "))

while (dividendo>0):
    dividendo-=divisor
    print(dividendo)

print(dividendo)
    