def solution(mats, park):
    answer = 0
    N,M=len(park),len(park[0])
    park=[[0]*(M+1)]+park
    for i in range(1,N+1):
        park[i]=[0]+park[i]
    for i in park:
        print(i)
    print(N,M)
    dp=[[0]*(M+1) for _ in range(N+1)]
    res=0
    for i in range(1,N+1):
        for j in range(1,M+1):
            if park[i][j]=="-1":
                dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                res=max(res,dp[i][j])
    print(res)
    mats.sort()
    for i in dp:
        print(i)
    v=-1
    for i in range(len(mats)):
        if mats[i]<=res:
            v=mats[i]
    return v