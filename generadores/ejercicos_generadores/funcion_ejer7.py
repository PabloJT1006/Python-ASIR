#.Dada una fórmula, guardar el resultado final y los dos resultados intermedios en 
#una matriz usando una librería externa

def F2 (numero1,numero2):
    return 18*numero1+2*numero2+25

def F1 (numero1,numero2,numero3,numero4):
    return (2*numero4+F2(numero1,numero2))/(2*numero1-3*numero3)

def EKIS(numero1,numero2,numero3,numero4):
    return (3*numero1+numero2)/(2*numero3-F1(numero1,numero2,numero3,numero4))+32

