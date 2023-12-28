class Moto():

    def __init__(self):
        self.color=""
        self.__ruedas=2
        self.motor=49
        self.arrancado=False
    
    def arrancar(self):
        self.arrancado=True

    def parar(self):
        self.arrancado=False

    def estado(self):
        print ("La moto es de color ",self.color,", tiene ",self.__ruedas," ruedas y tiene un motor de ",self.motor," cilindradas.")
        if(self.arrancado):
            print ("La moto está arrancada.")
        else:
            print ("La moto no está arrancada.")


print("-------------PRIMERA MOTO-------------")
moto1=Moto()
moto1.color="rojo"
moto1.estado()

print("-------------SEGUNDA MOTO-------------")
moto2=Moto()
moto2.color="amarillo"
moto2.__ruedas=4
moto2.arrancar()
moto2.estado()