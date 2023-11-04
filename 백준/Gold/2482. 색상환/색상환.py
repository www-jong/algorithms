import sys
input=sys.stdin.readline

N=int(input())
K=int(input())
dp=[[0]*(K+1) for _ in range(N+1)]
# dp[i][j]= i번째색상에서 j개색조합 가능한 수
# dp[i[j][0]= i번째 색상을 고르지 않았을 때 j개 구성수
for i in range(N+1):
    dp[i][1]=i
    dp[i][0]=1
for i in range(2,N):
    for j in range(2,min(i+1,K+1)):
        dp[i][j]=(dp[i-2][j-1]+dp[i-1][j])%1000000003
print((dp[N-1][K]+dp[N-3][K-1])%1000000003)