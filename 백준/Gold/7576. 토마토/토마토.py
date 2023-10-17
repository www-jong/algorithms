from collections import deque
import copy
n,m=map(int,input().split())
graph=[[3]*(n+1)]
for i in range(m):
    graph.append([3]+list(map(int,input().split())))
dx=[0,0,-1,1]
dy=[1,-1,0,0]
d=deque()
count=0
for aa in range(1,1+m):
    for bb in range(1,1+n):
        if graph[aa][bb]==1:
            d.append((aa,bb))
        else:continue
while d:
    q=copy.deepcopy(d)
    d.clear()
    while q:
        x,y=q.popleft()
        for i in range(4):
            sx=x+dx[i]
            sy=y+dy[i]
            if 1<=sx<=m and 1<=sy<=n:
                if graph[sx][sy]==0:
                    graph[sx][sy]=1
                    d.append((sx,sy))
    count+=1
ss=0
for li in graph:
    if 0 in li:
        print(-1)
        ss=1
        break
if ss==0:
    print(count-1)