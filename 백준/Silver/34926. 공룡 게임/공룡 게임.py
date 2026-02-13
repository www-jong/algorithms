N,K=map(int,input().split())
S='_'+input()
dp=[0]*(N+1)
dp[1]=1
for i in range(1,N+1):
    if dp[i]:
        if i+1<=N and S[i+1]=='_':
            dp[i+1]=1
        if i+K<=N and S[i+K]=='_':
            dp[i+K]=1
print('YES' if dp[N] else 'NO')