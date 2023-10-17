n=int(input())
def func2(n):
    dp=[1]*(n+1)
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
print("%d %d"%(func2(n),n-2))
