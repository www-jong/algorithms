def solution(numbers):
    answer = float('inf')
    cost=[[0]*10 for _ in  range(10)]
    tmp=[[]for _ in range(10)]
    tmp[0]=[3,1]
    for i in range(1,10):
        tmp[i]=[(i-1)//3,(i-1)%3]
    for i in range(10):
        for j in range(10):
            if i==j:
                cost[i][j]=1
            else:
                dr=abs(tmp[i][0]-tmp[j][0])
                dc=abs(tmp[i][1]-tmp[j][1])
                cost[i][j]=3*min(dr,dc)+2*abs(dr-dc)

    N=len(numbers)
    dp=[[[-1]*10 for _ in range(10)] for _ in range(N+1)]
    dp[0][4][6]=0
    for i in range(N):
        now=int(numbers[i])
        for j in range(10):
            for k in range(10):
                if dp[i][j][k]==-1:
                    continue
                if k!=now:
                    dp[i+1][now][k]=min(dp[i+1][now][k],dp[i][j][k]+cost[j][now]) if dp[i+1][now][k]!=-1 else dp[i][j][k]+cost[j][now]
                if j!=now:
                    dp[i+1][j][now]=min(dp[i+1][j][now],dp[i][j][k]+cost[k][now]) if dp[i+1][j][now]!=-1 else dp[i][j][k]+cost[k][now]

    for i in dp[N]:
        for j in i:
            if j!=-1:
                answer=min(answer,j)
    return answer