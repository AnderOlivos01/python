print("Introduzca el número de días:")
dias=input()
dias=int(dias)
print("Introduzca el día en el que empieza el mes (1 para LUNES, 7 para DOMINGO):")
inicio=input()
inicio=int(inicio)

print("LUNES MARTES MIÉRCOLES JUEVES VIERNES SÁBADO DOMINGO")
for i in range(dias):
    print()