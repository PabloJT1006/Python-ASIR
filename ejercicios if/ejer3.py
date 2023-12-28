#3. Introduce tres números y determina cuál es el mayor.

print("Introduce 3 numeros para comprobar cual es el mayor")

numero1=float(input("1º Introduce un numero: "))
numero2=float(input("2º Introduce un numero: "))
numero3=float(input("3º Introduce un numero: "))

if numero1>numero2:
    print("El mayor es el ",numero1)
elif numero1>numero3:
    print("El mayor es el ",numero1)
elif numero2>numero1:
    print("El mayor es el ",numero2)
elif numero2>numero3:
    print("El mayor es el ",numero2)
elif numero3>numero1:
    print("El mayor es el ",numero3)
elif numero3> numero2:
    print("El mayor es el ",numero3)