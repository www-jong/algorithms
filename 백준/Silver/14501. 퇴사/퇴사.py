n=int(input())
s=[[0,0]]
for i in range(n):
    s.append(list(map(int,input().split())))
dp=[[0]*6 for i in range(n+1)]
dp[1][s[1][0]]=s[1][1]

for i in range(2,n+1):
    if (n-i+1)>=s[i][0]:
        dp[i][s[i][0]]=max(dp[i-1][1]+s[i][1],dp[i-1][0]+s[i][1])
    dp[i][0]=max(dp[i-1][1],dp[i-1][0])
    for j in range(1,5):
        dp[i][j]=max(dp[i-1][j+1],dp[i][j])
print(max(dp[n][0],dp[n][1]))