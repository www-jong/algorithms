n=int(input())
d=list(map(int,input().split()))
dp=[0]*n
dp[0]=d[0]
for i in range(1,n):
    d[i]=max(d[i],d[i]+d[i-1])
print(max(d))