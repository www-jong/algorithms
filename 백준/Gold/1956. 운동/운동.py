import sys
INF=100000000000
V,E=map(int,input().split())
road=[[INF for i in range(V)] for i in range(V)]

for i in range(E):
  a,b,c=map(int,sys.stdin.readline().split())
  road[a-1][b-1]=c
dp=road
for k in range(V):
    for s in range(V):
        for e in range(V):
            dp[s][e]=min(dp[s][k]+dp[k][e],dp[s][e])
min_val=INF
for i in range(V):
    for j in range(V):
        min_val=min(min_val,dp[i][j]+dp[j][i])
if min_val==INF:
    print('-1')
else:
    print(min_val)