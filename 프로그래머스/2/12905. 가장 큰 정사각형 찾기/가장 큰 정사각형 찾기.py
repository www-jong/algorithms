def solution(board):
    res=0
    N,M=len(board),len(board[0])
    dp=[[0]*(M+1) for x in range(N+1)]

    for x in range(1,N+1):
        for y in range(1,M+1):
            if board[x-1][y-1]:
                dp[x][y]=min(dp[x-1][y],dp[x-1][y-1],dp[x][y-1])+1
                res=max(res,dp[x][y])
    return res**2