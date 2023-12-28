from funciones import cuadrado,triangulo,rectangulo

print("Introduce los datos para caluclar el area de las siguientes figuras")
print("------------------------------")
print("CUADRADO")
lad=float(input("Introduce el lado del cuadrado: "))
print("El area seria: ",cuadrado(lad))
print("--------------------------")
print("TRIANGULO")
bass=float(input("Introduce la base del triangulo: "))
alt=float(input("Introduce la altura del triangulo: "))
print("El area seria: ",triangulo(bass,alt))
print("-----------------------------------------")
print("RECTANGULO")
print("----------------------------------")
bassr=float(input("Introduce la base del rectangulo: "))
altr=float(input("Introduce la altura del rectangulo: "))
print("El area seria: ",rectangulo(bassr,altr))


