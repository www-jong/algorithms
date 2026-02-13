N,H=map(int,input().split())
li=[0]+list(map(int,input().split()))
dp=[0]*(N+1)
for i in range(1,N+1):
    dp[i]=dp[i-1]+li[i]
if H>dp[-1]:
    print(-1)
else:
    for i in range(1,N+1):
        if H<=dp[i]:
            print(i)
            break