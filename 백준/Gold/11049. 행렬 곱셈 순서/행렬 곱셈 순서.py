N=int(input())
li=[[0,0]]
for _ in range(N):
    li.append(list(map(int,input().split())))

dp=[[0]*(N+1) for i in range(N+1)]
# dp[i][j] --> i부터 j까지의 최소합
for i in range(1,N):
    dp[i][i+1]=li[i][0]*li[i][1]*li[i+1][1]

for i in range(2,N):
    for j in range(1,N+1-i):
        dp[j][i+j]=2**32
        for k in range(j,i+j):
            dp[j][i+j]=min(dp[j][i+j],dp[j][k]+dp[k+1][i+j]+li[j][0]*li[k][1]*li[j+i][1])
print(dp[1][N])