#4. Saca cuantas posiciones tienen datos en la lista, esto si se puede hacer tanto en listas, como tuplas, conjuntos y 
#arrays.
meses=["enero","febrero","marzo","abril","mayo","junio","agosto","septiembre","octubre","noviembre","diciembre"]
meses1=("enero","febrero","marzo","abril","mayo","junio","agosto","septiembre","octubre","noviembre","diciembre")
meses2={"enero","febrero","marzo","abril","mayo","junio","agosto","septiembre","octubre","noviembre","diciembre"}

meses3={"1":"enero","2":"febrero","3":"marzo","4":"abril","5":"mayo","6":"junio",
        "7":"agosto","8":"septiembre","9":"octubre","10":"noviembre","11":"diciembre"}

print("lista:", len(meses))
print("tupla:", len(meses1))
print("conjunto:", len(meses2))
print("diccionario:", len(meses3))