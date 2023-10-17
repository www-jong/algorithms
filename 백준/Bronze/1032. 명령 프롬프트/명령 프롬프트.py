t=int(input())
a=[]
for i in range(1,t+1):
    a.append(list(input()))
n=len(a[0])
for i in range(1,t):
    for j in range(0,n):
        a[0][j]=("?" if a[0][j]!=a[i][j] else a[0][j])
for i in range(0,n):
    print(a[0][i],end="")