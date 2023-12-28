#5. Introducir una nota numérica y devolver Suficiente, Notable, Bien, con switch.

nota=float(input("Introduce tu nota: "))

if nota < 5 :
    print("Has sacado un insuficiente")
elif nota>=5 and nota<7:
    print("Has sacado un suficiente")
elif nota>=7 and nota<9:
    print("Has sacado un notable")
elif nota>=9 and nota<=10:
    print("Has sacado un sobresaliente")
else:
    print("Introduce una nota valida")