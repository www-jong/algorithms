n=int(input())
dp=[[0]*10 for i in range(n+1)]
for i in range(1,10):
    dp[0][i]=1
    dp[1][i]=1
for i in range(2,n+1):
    dp[i][1]=dp[i-1][2]+dp[i-2][1]
    dp[i][9]=dp[i-1][8]
    for j in range(2,9):
        dp[i][j]=dp[i-1][j-1]+dp[i-1][j+1]
print(int(sum(dp[n])%1000000000))
