from cmath import sqrt

def segrado (a,b,c):
    x1= 0
    x2= 0
    if ((b**2)-4*a*c) < 0:
        return "La solución de la ecuación es con números complejos"
    else:
        x1 = (-b+sqrt(b**2-(4*a*c)))/(2*a)
        x2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)
        return "Las soluciones son: ",x1," y: ",x2
