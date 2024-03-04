L=[2,2,2,3,4,1,22,3]
apariciones=[]
for i in L:
    if L.count(i)>1:
        apariciones.append(i)
print(apariciones)