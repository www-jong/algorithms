n=int(input())
d=[0]*(31)
d[2]=3
for i in range(4,n+1,2):
    for j in range(2,i,2):
        d[i]+=d[i-j]*2
    d[i]+=2+d[i-2]
print(d[n])