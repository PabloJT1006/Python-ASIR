#Un programa que asigne a una variable multiplicar un número y me calculé su tabla de multiplicar



numero=int(input("Introduce un numero para calcular su tabla de multiplicar: "));



for x in range (1,11):
    print(numero, "*", x,"=" ,numero*x)