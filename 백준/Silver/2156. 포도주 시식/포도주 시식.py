import sys
n=int(sys.stdin.readline())
a=[0]
dp=[0]*(n+1)
dp[0]=0
for i in range(n):
    a.append(int(sys.stdin.readline()))
dp[1]=a[1]
if n>1:
    dp[2]=sum(a[1:3])
for i in range(3,n+1):
    dp[i]=max(dp[i-1],dp[i-3]+a[i-1]+a[i],dp[i-2]+a[i])
print(dp[n])