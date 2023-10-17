A=input()
B=input()
dp=[[[0,'']]*(len(B)+1) for i in range(len(A)+1)]
for i in range(1,len(A)+1):
    for j in range(1,len(B)+1):
        if A[i-1]==B[j-1]:
            dp[i][j]=[dp[i-1][j-1][0]+1,dp[i-1][j-1][1]+A[i-1]]
        else:
            if dp[i-1][j][0]>=dp[i][j-1][0]:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i][j-1]
if dp[-1][-1][0]==0:
    print(0)
else:
    print(dp[-1][-1][0])
    print(dp[-1][-1][1])