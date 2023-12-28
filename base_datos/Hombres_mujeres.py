

import mysql.connector #sin esto no funciona, pero antes debemos instalarlo con python -m pip install mysql-connector
import os #este se utiliza para los ficheros

rows = 0 #este es un contador de resultados obtenidos

#CREACIÓN DE LA BASE DE DATOS
	#EJERCICIO 1
bbdd = mysql.connector.connect(host="localhost", user="root", passwd="")

cursor = bbdd.cursor()
cursor.execute("drop database if exists personal_py")
cursor.execute("create database personal_py")

bbdd.close() #antes de abrir la bbdd, debemos crear una conexión, cerrarla, y luego abrirla ya iniciando con la bbdd

#CREACIÓN DE TABLAS E INSERCIÓN DE DATOS
bbdd = mysql.connector.connect(host="localhost", user="root", passwd="", database="personal_py")

fpersonal = open("personal.dat","r")
fhombres = open("hombres.dat","w")
fmujeres = open("mujeres.dat","w")

cursor = bbdd.cursor()
cursor.execute("drop table if exists hombre")
cursor.execute("create table hombre (dni varchar(9) primary key, nombre varchar(25), apellido varchar(25), edad int, sueldo int)")
cursor.execute("drop table if exists mujer")
cursor.execute("create table mujer (dni varchar(9) primary key, nombre varchar(25), apellido varchar(25), edad int, sueldo int)")

for x in fpersonal:
	linea = x.replace("\n","").split("\t") #el split convierte una línea en un array, separando cada las palabras según el carácter que indiquemos
	if (linea[4] == "H"):
		fhombres.write(linea[0] +"\t"+ linea[1] +"\t"+ linea[2] +"\t"+ linea[3] +"\t"+ linea[5] +"\n") #el salto de línea (\n) se pone automáticamente
		cursor.execute("insert into hombre (dni, nombre, apellido, edad, sueldo) values (%s,%s,%s,%s,%s)", (linea[0], linea[1], linea[2], linea[3], linea[5]))
		#se tiene que hacer así, si no, al menos los arrays no los reconoce (primero la sentencia sql, segundo los datos que insertamos)
		rows = rows+cursor.rowcount
	else:
		fmujeres.write(linea[0] +"\t"+ linea[1] +"\t"+ linea[2] +"\t"+ linea[3] +"\t"+ linea[5] +"\n")
		cursor.execute("insert into mujer (dni, nombre, apellido, edad, sueldo) values (%s,%s,%s,%s,%s)", (linea[0], linea[1], linea[2], linea[3], linea[5]))
		rows = rows+cursor.rowcount

print(rows," registro/s insertado/s.")
bbdd.commit() #importante ponerlo para actualizar las inserciones

#MODIFICACIÓN DE TABLAS
	#EJERCICIO 2
cursor.execute("update mujer set sueldo = sueldo*1.23 where sueldo < 600")
rows = cursor.rowcount
print(rows," registro/s actualizado/s.")
bbdd.commit()

cursor.execute("select * from mujer")
select = cursor.fetchall()
for x in select:
  print(x)

	#EJERCICIO 3
fapellidos = open("apellidos.dat","w")
cursor.execute("select dni, nombre, apellido, edad, sueldo/1.18 as sueldo from hombre where apellido = 'Peroto' or apellido like 'Pa%'")
select = cursor.fetchall()
for x in select:
	fapellidos.write(str(x[0]) +"\t"+ str(x[1]) +"\t"+ str(x[2]) +"\t"+ str(x[3]) +"\t"+ str(x[4]) +"\n") #de esta forma, la separación es también mediante tabuladores, como los otros ficheros

bbdd.close()
