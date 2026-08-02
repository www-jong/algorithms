inf=-float('inf')
N, T = map(int, input().split())
d=[]
for i in range(T+1):
    d.append((i,T-i))
grid = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j][0]= 타임머신 안쓴 최대값, dp[i][j][1]= 타임머신 쓴 최대값
dp1=[[inf]*(N+1) for _ in range(N+1)]
dp2=[[inf]*(N+1) for _ in range(N+1)]
dp1[1][1]=grid[0][0]

def func(x,y,c,v):
    if c==T:
        return v
    v1,v2=inf,inf
    if x<N:
        v1=func(x+1,y,c+1,v+grid[x][y-1])
    if y<N:
        v2=func(x,y+1,c+1,v+grid[x-1][y])
    return max(v1,v2)

# 1.오른쪽으로 채우고, 아래로 내려가면서 위,왼쪽값중 최대+현재칸
for x in range(1,N+1):
    for y in range(1,N+1):
        if x==1 and y==1:
            continue
        a=dp1[x-1][y] if x>1 else inf
        b=dp1[x][y-1] if y>1 else inf
        v=max(a,b)
        if v!=inf:
            dp1[x][y]=grid[x-1][y-1]+v
            v=func(x,y,0,dp1[x][y])
            dp2[x][y]=v+grid[x-1][y-1]

for x in range(1,N+1):
    for y in range(1,N+1):
        if x>1 and dp2[x-1][y]!=inf:
            dp2[x][y]=max(dp2[x][y],dp2[x-1][y]+grid[x-1][y-1])
        if y>1 and dp2[x][y-1]!=inf:
            dp2[x][y]=max(dp2[x][y],dp2[x][y-1]+grid[x-1][y-1])

print(max(dp1[N][N],dp2[N][N]))
