#11.Igual al anterior pero meter el nombre de las mujeres en un nuevo array
nombres=["Juan","Pablo","Maria","Anabel","Rigoberta","Adonis"]
sexo=["M","M","F","F","F","M"]
mujeres=[]
for i in range(0,len(nombres)):
    if (sexo[i]=="F"):
        mujeres.append(nombres[i])

print ("Lista de mujeres: ",mujeres)