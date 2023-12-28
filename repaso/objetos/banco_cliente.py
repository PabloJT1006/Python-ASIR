#bacno ssolo tiene tres clientes
import random


class CLIENTE():
    def __init__(self,nombre):
        self.nombre=nombre
        self.cantidad=0
    
    def depositar(self,cantiad):
        self.cantidad+=cantiad
    
    def extraer(self,cantidad):
        self.cantidad-=cantidad
    
    def mostrar(self):
        print ("El cliente ",self.nombre," tiene ",self.cantidad)
    

class BANCO():
    def __init__(self):
        self.cliente1= CLIENTE("RUBEN")
        self.cliente2= CLIENTE("RODOLFO")
        self.cliente3= CLIENTE("MIGUEL")

    def operar(self):
        self.cliente1.depositar(random.randint(200,1000))
        self.cliente2.depositar(random.randint(200,1000))
        self.cliente3.depositar(random.randint(200,1000))
        self.cliente1.extraer(random.randint(200,1000))
        self.cliente2.extraer(random.randint(200,1000))
    
    def deposito_total(self):
        total=self.cliente1.cantidad+self.cliente2.cantidad+self.cliente3.cantidad
        self.cliente1.mostrar()
        self.cliente2.mostrar()
        self.cliente3.mostrar()
        print ("La cantidad total que hay depositada en el banco es de: ",total)



banco=BANCO()

banco.operar()

banco.deposito_total()

