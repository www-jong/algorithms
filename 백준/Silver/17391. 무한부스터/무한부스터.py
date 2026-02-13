from collections import deque
import sys
input=sys.stdin.readline
d=[(0,1),(1,0)]
N,M=map(int,input().split())
li=[list(map(int,input().split())) for _ in range(N)]
visit=[[0]*M for _ in range(N)]
visit[0][0]=0
q=deque()
q.append((0,0))

while q:
    x,y=q.popleft()
    for i in range(2):
        nx,ny=x,y
        for j in range(li[x][y]):
            nx,ny=nx+d[i][0],ny+d[i][1]
            if 0<=nx<N and 0<=ny<M and visit[nx][ny]==0:
                q.append((nx,ny))
                visit[nx][ny]=visit[x][y]+1
print(visit[-1][-1])