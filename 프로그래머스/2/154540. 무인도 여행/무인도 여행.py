from collections import deque
def solution(maps):
    answer = []
    dir=[0,0,1,-1]
    N,M=len(maps),len(maps[0])
    visit=[[0]*M for _ in range(N)]
    d={}
    idx=0
    for i in range(N):
        for j in range(M):
            if visit[i][j] or maps[i][j]=='X':
                continue
            idx+=1
            visit[i][j]=idx
            q=deque()
            q.append((i,j))
            d[idx]=int(maps[i][j])
            while q:
                x,y=q.popleft()
                for k in range(4):
                    nx,ny=x+dir[k],y+dir[3-k]
                    if 0<=nx<N and 0<=ny<M and not visit[nx][ny] and maps[nx][ny]!='X':
                        visit[nx][ny]=idx
                        d[idx]+=int(maps[nx][ny])
                        q.append((nx,ny))
    answer=sorted([i for i in d.values()])
    return answer if answer else [-1]