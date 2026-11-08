from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    d=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
    d2=[(0,1),(0,-1),(1,0),(-1,0)]
    li=[[0]*102 for _ in range(102)]
    for rec in rectangle:
        x1,y1,x2,y2=[i*2 for i in rec]
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                if x==x1 or x==x2 or y==y1 or y==y2:
                    li[x][y]=1
    visit=[[0]*102 for _ in range(102)]
    q=deque()
    q.append((0,0))
    visit[0][0]=1
    while q:
        x,y=q.popleft()
        for dx,dy in d:
            nx,ny=x+dx,y+dy
            if 0<=nx<=101 and 0<=ny<=101 and not visit[nx][ny]:
                visit[nx][ny]=1
                if li[nx][ny]==1:
                    li[nx][ny]=2
                else:
                    q.append((nx,ny))
    visit=[[-1]*102 for _ in range(102)]
    q=deque()
    q.append((characterX*2,characterY*2))
    visit[0][0]=0
    while q:
        x,y=q.popleft()
        for dx,dy in d2:
            nx,ny=x+dx,y+dy
            if 0<=nx<=101 and 0<=ny<=101 and visit[nx][ny]==-1 and li[nx][ny]==2:
                visit[nx][ny]=visit[x][y]+1
                q.append((nx,ny))

    return (visit[itemX*2][itemY*2]+1)//2