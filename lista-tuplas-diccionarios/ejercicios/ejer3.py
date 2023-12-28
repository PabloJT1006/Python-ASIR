#3. Sacar todos los datos de una lista con un bucle.
meses=["enero","febrero","marzo","abril","mayo","junio","agosto","septiembre","octubre","noviembre","diciembre"]
meses1=("enero","febrero","marzo","abril","mayo","junio","agosto","septiembre","octubre","noviembre","diciembre")
meses2={"enero","febrero","marzo","abril","mayo","junio","agosto","septiembre","octubre","noviembre","diciembre"}

meses3={"1":"enero","2":"febrero","3":"marzo","4":"abril","5":"mayo","6":"junio",
        "7":"agosto","8":"septiembre","9":"octubre","10":"noviembre","11":"diciembre"}
for i in meses:
    print(i)
print("-----------------------------------------------")
for j in meses1:
    print(j)
print("-----------------------------------------------")

for x in meses2:
    print(x)
print("-----------------------------------------------")

for y in meses3.items():
    print(y)




