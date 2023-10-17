n=int(input())
a=[0]+list(map(int,input().split()))
dp1=[0]*(n+1)
dp1[0]=0
for i in range(1,n+1):
    for j in range(i):
        if a[j]<a[i] and dp1[i]<dp1[j]: 
            dp1[i]=dp1[j]
    dp1[i]+=1
print(max(dp1))