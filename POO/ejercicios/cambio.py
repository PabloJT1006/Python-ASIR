class cambio():
    def __init__(self):
        self.monedas=0
    
    def moneda_euro (self):
        self.monedas*=1.5
    
    def euro_moneda(self):
        self.monedas/=1.5
    
    def estado(self):
        print ("Su menoda se ha cmabiado correctamente y ahora tienes: ",self.monedas)


money=float(input("Introduzca una cantidad de dinero: "))
cambiar=cambio()
cambiar.monedas=money

opc=int(input("Quieres cambiar de moneda a euro o de euro a moneda (1/2)"))

if (opc==1):
    cambiar.moneda_euro()
    cambiar.estado()
    print ("euro")

elif(opc==2):
    cambiar.euro_moneda()
    cambiar.estado()
    print ("monedas")

else:
    print ("Opcion invalidada haber estudiao")





