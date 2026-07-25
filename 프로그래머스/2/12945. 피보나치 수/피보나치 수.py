def solution(n):
    answer = 0
    dp=[0]*(n+1)
    dp[2]=1
    dp[3]=2
    for i in range(4,n+1):
        dp[i]=(dp[i-1]+dp[i-2])%1234567
    return dp[n]