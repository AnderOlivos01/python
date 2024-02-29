print("Introduzca el número de días:")
dias=input()
dias=int(dias)
print("Introduzca el día en el que empieza el mes (1 para LUNES, 7 para DOMINGO):")
inicio=input()
inicio=int(inicio)
colactual=inicio
print("LUN MAR MIE JUE VIE SÁB DOM")
print(" "*4*(inicio-1),end="")
for i in range(dias):
    if colactual==8:
        print("")
        colactual=1
    print("{:3} ".format(i+1),end="")
    colactual=colactual+1
    