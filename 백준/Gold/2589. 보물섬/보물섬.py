from collections import deque
N,M=map(int,input().split())
li=[]
for i in range(N):
    li.append(input())
d=[0,0,1,-1]

def func(i,j):
    q=deque()
    q.append((i,j))
    visit=[[0]*M for _ in range(N)]
    visit[i][j]=1
    tmp=0
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+d[i],y+d[3-i]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            elif li[nx][ny]=='L' and not visit[nx][ny]:
                visit[nx][ny]=visit[x][y]+1
                tmp=max(tmp,visit[nx][ny])
                q.append((nx,ny))
    return tmp-1
res=0
for i in range(N):
    for j in range(M):
        if li[i][j]=='L':
            res=max(res,func(i,j))
print(res)