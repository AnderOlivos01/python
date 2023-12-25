invertida=''
print("Escriba una palabra o frase:")
palabra = input()
for i in range(len(palabra)-1,-1,-1):
    invertida=invertida+palabra[i]
print("La palabra/frase invertida es: ",invertida)