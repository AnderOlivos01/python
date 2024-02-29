print("¡Bienvenido a Lingo!")
palabra="ABUELA"
print("Introduzca una palabra con 6 letras.")
for a in range (8):
    intento=input().upper()
    if len(intento)!=len(palabra):
        print("..................")
    else:
        for i in range (len(palabra)):
            if palabra[i]==intento[i]:
                print
    if intento==palabra:
        print("HA GANADO")
        
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