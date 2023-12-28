#1. Introducir un número y determinar si está comprendido entre 1 y 10.
print("Introduce un numero para comprobar que esta comprendido entre 1 y 10")
numero=float(input("Introduce un numero: "))

if numero>=1 and numero<=10:
    print(numero," esta comprendido entre 1 y 10")
else:
    print(numero," esta fuera de rango")