n, m = map(int, input().split())
grid = [[0]*(m+1)]+[[0]+list(map(int, input().split())) for _ in range(n)]

for i in range(1,n+1):
    for j in range(1,m+1):
        grid[i][j]=0 if grid[i][j]>0 else 1
# Please write your code here.
dp=[[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j]=grid[i][j]+dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]

res = -1

for h in range(1, n+1):
    for w in range(1, m+1):
        for x in range(1, n-h+2):
            for y in range(1, m-w+2):
                nx, ny = x+h-1, y+w-1

                cnt = dp[nx][ny]-dp[x-1][ny]-dp[nx][y-1]+dp[x-1][y-1]

                if cnt == 0:
                    res = max(res, h*w)

print(res)