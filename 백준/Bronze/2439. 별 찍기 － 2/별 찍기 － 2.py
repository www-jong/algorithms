a=int(input())
for i in range(1,a+1):
    for j in range(a,i,-1):
        print(" ",end="")
    for i in range(1,i+1):
        print("*",end="")
    print()