print("¡Bienvenido al juego del ahorcado!")
print("Introduzca una letra y luego pulse le tecla intro.")
palabra="HUEVO"
for a in range (6):
    letra1=input().upper()
    if (letra1 in palabra) == True:
        ind1=palabra.index(letra1)
        if ind1>0:
            print("# "*(ind1),end="")
        print(letra1,end=" ")
        if ind1<len(palabra):
            print("# "*(len(palabra)-ind1-1))
    else:
        print("# "*(len(palabra)))
print("Proponga una palabra")
propuesta=input().upper()
if propuesta==palabra:
    print("HA GANADO")
else:
    print("HA PERDIDO, LA PALABRA ERA "+palabra)