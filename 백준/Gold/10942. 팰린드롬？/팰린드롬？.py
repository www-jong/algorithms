import sys
n=int(sys.stdin.readline())
arr=[0]+list(map(int,sys.stdin.readline().split()))
m=int(input())
dp=[[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1,n+1):
    dp[i][i]=1
for i in range(1,n):
    if arr[i]==arr[i+1]:
        dp[i][i+1]=1
for i in range(2,n):
    for j in range(1,n+1-i):
        if dp[j+1][j+i-1]==1 and arr[j]==arr[j+i]:
            dp[j][j+i]=1
for i in range(m):
    q,w=map(int,sys.stdin.readline().split())
    print(dp[q][w])
