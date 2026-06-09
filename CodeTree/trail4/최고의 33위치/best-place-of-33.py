n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp=[[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j]=grid[i-1][j-1]+dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]

res=0

for i in range(3,n+1):
    for j in range(3,n+1):
        now=dp[i][j]-dp[i-3][j]-dp[i][j-3]+dp[i-3][j-3]
        res=max(res,now)
print(res)