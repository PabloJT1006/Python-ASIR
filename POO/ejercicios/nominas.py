
class Nomina():
     
    def __init__(self):

     self.sueldo = 1000
     self.hijo = 0
     self.categoria = 0
     self.comision = 0
     self.sueldoBruto = 0

    def nombre(self):
        self.nombre=input("Introduce el nombre del empleado:")

    def daCategoria(self):
        self.categoria= int(input("Introduce la categoria del empleado(1 o 2): "))

    def daSueldoBrutoInicial(self):
        if (self.categoria==1):
            return self.sueldo + 500
        elif (self.categoria==2):
            return  self.sueldo +250
    

    def daComision(self):
        self.comision=int(input("Introduce la comisión: "))

    def numHijos(self):
        try:
          self.hijo=int(input("Introduce el número de hijos: "))
        except ValueError:
            return("Introduce un número correcto")

    def daSueldoBruto(self):
         self.sueldoBruto = self.daSueldoBrutoInicial()+ self.comision +self.hijo*100

    def daIrpf(self):
        if (self.sueldoBruto < 1500):
            return self.sueldoBruto*10/100
        elif (self.sueldoBruto >= 1500 and self.sueldoBruto <1700):
            return self.sueldoBruto*14/100
        elif (self.sueldoBruto >= 1700):
            return self.sueldoBruto*20/100
            
    def daSueldoNeto(self):
        if (self.sueldoBruto < 1500):
            return self.sueldoBruto*0.90
        elif (self.sueldoBruto >= 1500 and self.sueldoBruto <1700):
            return self.sueldoBruto*0.86
        elif (self.sueldoBruto >= 1700):
            return self.sueldoBruto*0.80 
            

    
    def estado(self):
        print("-------------------------------------------") 
        print("Nombre del empleado: ",self.nombre)
        print("Categoria: ",self.categoria)
        print("Sueldo Bruto Inicial: ",self.daSueldoBrutoInicial())
        print("Comisión: ",self.comision)
        print("Número de hijos:  ",self.hijo)
        print("Sueldo Bruto:  ",self.sueldoBruto)
        print("Irpf: ",self.daIrpf())
        print("Sueldo Neto: ",self.daSueldoNeto()) 

           

empleado1=Nomina()
empleado1.nombre()
empleado1.daCategoria()
empleado1.daSueldoBrutoInicial()
empleado1.daComision()
empleado1.numHijos()
empleado1.daSueldoBruto()
empleado1.daIrpf()
empleado1.daSueldoNeto()
empleado1.estado()
    