n=int(input())
a=[0]+list(map(int,input().split()))+[0]
dp1=[0]*(n+1)
dp2=[0]*(n+2)
dp1[0],dp2[n+1]=0,0
for i in range(1,n+1):
    for j in range(i):
        if a[j]<a[i] and dp1[i]<dp1[j]:
            dp1[i]=dp1[j]
    dp1[i]+=1
for i in range(n,0,-1):
    for j in range(n+1,i-1,-1):
        if a[j]<a[i] and dp2[i]<dp2[j]:
            dp2[i]=dp2[j]
    dp2[i]+=1
max=-3000
for i in range(1,n+1):
    if dp1[i]+dp2[i]-1>max:
        max=dp1[i]+dp2[i]-1
print(max)