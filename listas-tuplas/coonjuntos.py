

semana = {"lunes", "martes", "miercoles", "jueves","viernes","sabado","domingo"}
print (semana)

for j in semana:
    print(j)

print("sabado" in semana)
print("septiembre" in semana)

semana.add("septiembre")
print(semana)

semana.update(["octubre","septiembre","noviembre"])
print(semana)

print(len(semana))
semana.clear
print(semana)
semana.add("martes")
print(semana)
del semana
print(semana)

