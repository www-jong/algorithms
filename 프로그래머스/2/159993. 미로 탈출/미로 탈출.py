from collections import deque
def solution(maps):
    d=[0,0,1,-1]
    def func(st,end):
        visit=[[-1]*M for _ in range(N)]
        visit[st[0]][st[1]]=0
        q=deque()
        q.append((*st,0))
        while q:
            x,y,c=q.popleft()
            for i in range(4):
                nx,ny=x+d[i],y+d[3-i]
                if 0<=nx<N and 0<=ny<M and maps[nx][ny]!='X' and (visit[nx][ny]==-1 or visit[nx][ny]>c+1):
                    q.append((nx,ny,c+1))
                    visit[nx][ny]=c+1
        return visit[end[0]][end[1]]
    answer = 0
    st,mid,end=0,0,0
    N,M=len(maps),len(maps[0])
    for i in range(N):
        for j in range(M):
            if maps[i][j]=='S':
                st=[i,j]
            if maps[i][j]=='E':
                end=[i,j]
            if maps[i][j]=='L':
                mid=[i,j]
    r1=func(st,mid)
    if r1==-1:
        return -1
    r2=func(mid,end)
    if r2==-1:
        return -1
    return r1+r2