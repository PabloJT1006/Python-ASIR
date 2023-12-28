#25. Tomando del teclado el precio por unidad de un determinado producto, se pretende 
# imprimir un listado con los precios para unidades desde 1 a 100. Se deben aplicar una serie de
# descuentos, a saber: 10% a partir de 15 unidades, 15% a partir de 30 unidades, 20% a partir 
# de 50 unidades.


bucle=True

while (bucle):
    precio=float(input("Introduce el precio por unidad del producto: "))
    cantidad=int(input("Introduce la cantidad entre 1 y 100: "))
    if cantidad>=1 and cantidad<=100:
        bucle=False
        if(cantidad>=15 and cantidad<30):
            precio*=0.9
            print("Se le ha aplicado un descuento del 10% al ser mas de 15 unidades: ",precio," por unidad y precio total: ",precio*cantidad)

        elif (cantidad>=30 and cantidad<50):
            precio*=0.85
            print("Se le ha aplicado un descuento del 15% al ser mas de 30 unidades: ",precio," por unidad y precio total: ",precio*cantidad)

        elif (cantidad>=50 and cantidad<=100):
            precio*=0.8
            print("Se le ha aplicado un descuento del 20% al ser mas de 50 unidades: ",precio," por unidad y precio total: ",precio*cantidad)
        
    else:
        print("Introduce una cantidad entre 1 y 100")
        bucle=True

