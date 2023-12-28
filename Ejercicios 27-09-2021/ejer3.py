#Un programa que se introduzca una cantidad numérica en una variable y calculemos un IVA del 16 del 30 y 3 y del 72% qué debe ser mostrado en pantalla

numero=float(input("Introduce el precio para calcularle la posible cantidad de IVA añadida: "))

iva1=numero*1.16
iva2=numero*1.3
iva3=numero*1.03
iva4=numero*1.72

print("Aplicando el 16% de IVA este seria el precio: ", iva1)
print("Aplicando el 30% de IVA este seria el precio: ", iva2)
print("Aplicando el 3% de IVA este seria el precio: ", iva3)
print("Aplicando el 72% de IVA este seria el precio: ", iva4)



