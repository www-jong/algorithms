def solution(n, money):
    answer = 0
    N=len(money)
    dp=[0]*(n+1)
    dp[0]=1
    for i in money:
        for j in range(n):
            if j+i<=n:
                dp[i+j]+=dp[j]
                dp[i+j]%=1000000007
                
    return dp[n]