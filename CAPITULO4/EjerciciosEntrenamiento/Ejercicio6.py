for i in range (1,100):
    primo=True
    for a in range (2,i):
        if i%a==0:
            primo=False
    if primo:
        print(i,end=" ")
