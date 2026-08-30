def solution(sticker):
    N=len(sticker)
    if N==1:
        return sticker[0]
    dp=[[0,0] for _ in range(N)]
    dp[0][1]=sticker[0]
    dp[1][1]=sticker[0]
    dp[1][0]=sticker[1]
    for i in range(2,N):

        if i!=N-1:
            dp[i][1]=max(dp[i-1][1],dp[i-2][1]+sticker[i])
        dp[i][0]=max(dp[i-1][0],dp[i-2][0]+sticker[i])
    return max(dp[N-2][1],dp[N-1][0])