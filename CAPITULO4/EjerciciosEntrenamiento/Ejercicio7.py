L=[1,5,11,19,8,50,77]
for i in range(len(L)-1):
    if L[i]>L[i+1]:
        print("Error en la posición ",i+1," de L.")
    