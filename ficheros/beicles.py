# Dado un fichero llamado vehículos. Dicho fichero tiene, matrícula, tipo (coche, moto, camión), 
# precio y el consumo
# (5/10/20 registros) una vez creado leemos el fichor. Si es Camión sacar al menos 2 en pantalla, si 
# es moto y el precio es menos de 3000 euros lo grabamos en una lista. Si es coche, se guarda en un 
# fichero denominado ficheroCoches.py
# el cual iremos añadiendo todos los coches que vayan saliendo.
# Sacar la lista de las motos en pantalla y los coches de su fichero.
import  random


fichero=open("vehiculos.txt","w")

for x in range(100):
    matricula=random.randint(10000,99999)
    tipo = random.randint(1,3)
    precio = random.randint(1000,10000)
    consumo = random.randint(10,100)
    fichero.write("%d\t%d\t%d\t%d\n" %(matricula,tipo,precio,consumo))
fichero.close()
