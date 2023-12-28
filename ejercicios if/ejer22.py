#22. Realizar el programa que muestre por pantalla la tabla de multiplicar de un número dado.
# La salida del programa deberá ser de la siguiente forma:
multiplicador=0
multiplicando=int(input("Introduce un numero para clacular su tabla de multiplicar: "))

while (multiplicador<10):
    multiplicador+=1
    producto=multiplicando*multiplicador
    print(multiplicando,"*",multiplicador,"=",producto)