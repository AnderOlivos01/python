L=[22,342,2452,645346,745,7457,54645,64564,56452,52,5235,253,235465346,34634,6346,34,3]
pares=[]
impares=[]
for i in L:
    if i%2==0:
        pares.append(i)
    else:
        impares.append(i)
print("PARES: ",pares)
print("IMPARES: ",impares)       
