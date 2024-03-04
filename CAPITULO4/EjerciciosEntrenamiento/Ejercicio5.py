import math
def pol (a,b,c):
    tri=(b*b)-(4*a*c)
    if tri > 0:
        res1=(-b+math.sqrt(tri))/(2*a)
        res2=(-b-math.sqrt(tri))/(2*a)
        res=[res1,res2]
        return res
    if tri == 0:
        return (-b/(2*a))
    if tri < 0:
        return False
print("Introduzca los valores del polinomio separados por espacios(ax^2+bx+c). Ejemplo: 10 2 2")
ent=input().split(" ")
raices=pol(int(ent[0]),int(ent[1]),int(ent[2]))    
if raices == False:
    print("No hay ninguna solución")
else:
    print(raices)