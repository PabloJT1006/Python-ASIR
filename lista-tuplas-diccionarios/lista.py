meses=["enero","febrero","marzo","abril","mayo","junio","agosto","septiembre","octubre","noviembre","diciembre"]

dias=("lunes","martes","miercoles","jueves","viernes","sabado","domingo")

print(meses)
print(dias)

print(meses[3])
print(dias[3])

meses.append("neptuno")
print(meses[11])

#dias.append("neptuno")

meses.insert(5,"urano")
#dias.insert(5,"urano")
print(meses)

meses.pop()
print(meses)
#dias.pop()

meses.reverse()
print(meses)

meses.pop(3)
print(meses)

meses.clear()
print(meses)

#dias.clear()