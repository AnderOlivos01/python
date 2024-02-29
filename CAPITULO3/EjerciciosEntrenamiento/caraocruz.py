import random
print("El 0 es la CRUZ y el 1 la CARA")
print("Escriba el número de tiradas de la moneda:")
tiradas=int(input())
cara=0
cruz=0
for i in range(tiradas):
    nran=random.randint(0,1)
    if nran==0:
        cruz=cruz+1
    if nran==1:
        cara=cara+1
pcara=int((100*cara)/tiradas)
pcruz=int((100*cruz)/tiradas)
print("PORCENTAJE DE CRUZ: {0}%".format(pcruz))
print("PORCENTAJE DE CARA: {0}%".format(pcara))