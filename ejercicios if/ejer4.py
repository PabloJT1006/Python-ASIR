#4. Introduce tres números y muéstralos ordenados de menor a mayor.

print("Introduce 3 numeros para comprobar cual es el mayor")

numero1=float(input("1º Introduce un numero: "))
numero2=float(input("2º Introduce un numero: "))
numero3=float(input("3º Introduce un numero: "))

if numero1>numero2 and numero2>numero3:
    print(numero1,", ",numero2,", ",numero3)
elif numero2>numero1 and numero1>numero3:
    print(numero2,", ",numero1,", ",numero3)
elif numero2>numero3 and numero3>numero1:
    print(numero2,", ",numero3,", ",numero1)
elif numero3>numero2 and numero2>numero1: 
    print(numero3,", ",numero2,", ",numero1)
elif numero3>numero1 and numero1>numero2:
    print(numero3,", ",numero1,", ",numero2)
elif numero1> numero3 and numero3>numero2:
    print(numero1,", ",numero3,", ",numero2)
