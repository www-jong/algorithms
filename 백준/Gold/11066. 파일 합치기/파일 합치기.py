import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    K=int(input())
    li=[0]+list(map(int,input().split()))
    dp=[[0]*(K+1) for _ in range(K+1)]
    sums=[0]*(K+1)
    for i in range(1,K):
        dp[i][i+1]=li[i]+li[i+1]
        sums[i]=sums[i-1]+li[i]
    sums[K]=sums[K-1]+li[K]
    for k in range(2,K+1):
        for i in range(1,K+1):
            if i+k>K:
                break
            min_v=10**9
            for j in range(i,i+k):
                min_v=min(min_v,dp[i][j]+dp[j+1][i+k])
            dp[i][i+k]=min_v+sums[i+k]-sums[i-1]
    print(dp[1][K])