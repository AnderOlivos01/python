L1=[1,4,10,20]
L2=[2,3,5]
L3=L1.copy()
for i in L2:
    if (i in L3)==False:
        L3.append(i)
print(sorted(L3))