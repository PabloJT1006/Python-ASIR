from funciones import descuento

print("Introduce el precio de un producto con su respectivo descuento")

prduct=float(input("Introduce el precio del producto: "))
porcen=int(input("Introduce el porcentaje a rebajar: "))
print("El precio final del producto seria de: ",descuento(prduct,porcen))
