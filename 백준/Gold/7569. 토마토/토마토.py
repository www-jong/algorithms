from collections import deque
import copy
n,m,h=map(int,input().split())
graph=[[3]]
for j in range(h):
    ssss=[[3]*(n+1)]
    for i in range(m):
        ssss.append([3]+list(map(int,input().split())))
    graph.append(ssss)
dx=[0,0,1,-1,0,0]
dy=[1,-1,0,0,0,0]
dz=[0,0,0,0,1,-1]
d=deque()
count=0
for aa in range(1,1+m):
    for bb in range(1,1+n):
        for cc in range(1,1+h):
            if graph[cc][aa][bb]==1:
                d.append((cc,aa,bb))
            else:continue
while d:
    q=copy.deepcopy(d)
    d.clear()
    while q:
        z,x,y=q.popleft()
        for i in range(6):
            sz=z+dz[i]
            sx=x+dx[i]
            sy=y+dy[i]
            if 1<=sx<=m and 1<=sy<=n and 1<=sz<=h:
                if graph[sz][sx][sy]==0:
                    graph[sz][sx][sy]=1
                    d.append((sz,sx,sy))
    count+=1
ss=0
for zz in range(1,h+1):
    for xx in range(1,1+m):
        for yy in range(1,1+n):
            if 0==graph[zz][xx][yy] and ss==0:
                print(-1)
                ss=1
                break
            else:continue
if ss==0:
    print(count-1)