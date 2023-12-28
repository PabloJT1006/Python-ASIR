#10.Crear un array con nombres de personas y otro con sus sexos y sacar el nombre de las mujeres

nombres=["Juan","Pablo","Maria","Anabel","Rigoberta","Adonis"]
sexo=["M","M","F","F","F","M"]

for i in range(0,len(nombres)):
    if (sexo[i]=="F"):
        print("Mujer: ",nombres[i])

