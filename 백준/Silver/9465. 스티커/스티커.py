for _ in range(int(input())):
    n=int(input())
    lis=[]
    for _ in range(2):
        lis.append([0]+list(map(int,input().split())))
    dp=[[0,0,0] for i in range(n+1)]
    dp[1][0]=0
    dp[1][1]=lis[0][1]
    dp[1][2]=lis[1][1]
   
    for i in range(2,n+1):
        dp[i][0]=max(dp[i-1][0],dp[i-1][1],dp[i-1][2])
        dp[i][1]=max(dp[i-1][0],dp[i-1][2])+lis[0][i]
        dp[i][2]=max(dp[i-1][0],dp[i-1][1])+lis[1][i]
    print(max(dp[n]))