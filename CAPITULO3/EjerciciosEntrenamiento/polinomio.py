#Calcular el valor del polinomio 3x^2+5x+1
import math
def pol(a,b,c):
    resultado1=(-b+math.isqrt(b*b-4*a*c))/(2*a)
    resultado2=(-b-math.isqrt(b*b-4*a*c))/(2*a)
    print (resultado1)
    print(resultado2)
    
    
pol(3,5,1)