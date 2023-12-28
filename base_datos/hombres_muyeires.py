from sqlite3 import Cursor
import mysql.connector
bbdd = mysql.connector.connect(host="localhost", user="root", passwd="",database="persona")
cursor=bbdd.cursor()
cursor.execute("create table hombre(dni varchar(9) primary key,nombre varchar(25),apellido varchar (25),edad int, sueldo int)")
omvres=open("personal.txt","r").readlines()




