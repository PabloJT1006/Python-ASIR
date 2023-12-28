


while True:
    try:
        precio=float(input("Introduce el precio de una unidad  para ver el listado de precios"))
        break
    except ValueError:
        print("Los valores introducidos no son correctos")

pre1=precio-precio*0.1
pre2=precio-precio*0.15
pre3=precio-precio*0.2

print("Si compras 15: ",pre1," si compras 30: ",pre2," si compras: ",pre3)