alumnos={
"matricula": "111",
"nombre": "roy",
"apellidos": "mustang",
"direccion":"calle algarrobo",
"edad": "25" ,
"sexo":"indefinido"
}
print(alumnos)

x=alumnos["direccion"]
print (x)



alumnos["edad"]=30
print(alumnos)

for i in alumnos:
    print(i,":",alumnos[i])

for i in alumnos.values():
    print (i)


for i in alumnos.items():
    print (i)

if "apellidos" in alumnos:
    print("apellido dentro del dic")