from collections import deque
d=[0,0,1,-1]
N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
li=[[{0:-1} for _ in range(N)] for _ in range(N)]
res=10**9


for t in range(K-1):
    for x in range(N):
        for y in range(N):
            if t in li[x][y]:
                for k in range(4):
                    nx,ny=x+d[k],y+d[3-k]
                    if 0<=nx<N and 0<=ny<N and grid[nx][ny]>grid[x][y]:
                        if t+1 in li[nx][ny]:
                            li[nx][ny][t+1]=min(li[nx][ny][t+1],max(li[x][y][t],grid[nx][ny]-grid[x][y]))
                        else:
                            li[nx][ny][t+1]=max(li[x][y][t],grid[nx][ny]-grid[x][y])

for x in range(N):
    for y in range(N):
        if K-1 in li[x][y]:
            res=min(res,li[x][y][K-1])

print(res if res!=10**9 else -1)