import sys
input=sys.stdin.readline

N,M=map(int,input().split())
li=[input().rstrip() for _ in range(N)]
dp=[[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if li[i][j]=='1':
            if i==0 or j==0:
                dp[i][j]=1
            else:
                if dp[i-1][j]==dp[i][j-1]:
                    if li[i-dp[i][j-1]][j-dp[i][j-1]]=='1':
                        dp[i][j]=dp[i-1][j]+1
                    else:
                        dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1])+1

                    
print(max([max(i) for i in dp])**2)
