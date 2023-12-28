class Calculadora():
    def __init__(self):
        self.resultado=0
        

        

    def suma (self,a,b,indice):
        self.resultado=a+b
        indice+=1

    def resta (self,a,b):
        self.resultado=a-b
        self.indice+=1
    
    def division (self,a,b):
        self.resultado=a/b
        self.indice+=1

    def multiplicacion (self,a,b):
        self.resultado=a*b
        self.indice+=1 

    def estado (self):
        print ("El resultado seria: ",self.resultado[0])


numero1=float(input("Introduzca un numero: "))
numero2=float(input("Introduzca un numero: "))

print("-----------CALCULADORA UNO---------------------")
casio=Calculadora()
casio.division(numero1,numero2)
casio.estado()
casio.resta(numero1,numero2) 
casio.estado()

print("-----------CALCULADORA DOS---------------------")
YAMAHA=Calculadora()
YAMAHA.suma(numero1,numero2)
YAMAHA.estado()

#YAMAHA.multiplicacion(numero1,numero2)
casio.estado()



