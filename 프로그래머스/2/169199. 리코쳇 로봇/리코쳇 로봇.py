from collections import deque
def solution(board):
    N,M=len(board),len(board[0])
    d=[0,0,1,-1]
    st,end=0,0
    for i in range(N):
        for j in range(M):
            if board[i][j]=='R':
                st=[i,j]
            if board[i][j]=='G':
                end=[i,j]
    res=10**9
    visit=[[-1]*M for _ in range(N)]
    q=deque()
    visit[st[0]][st[1]]=0
    q.append((*st,0))
    while q:
        x,y,c=q.popleft()
        for i in range(4):
            nx,ny=x,y
            while True:
                nx+=d[i]
                ny+=d[3-i]
                if 0<=nx<N and 0<=ny<M and board[nx][ny]!='D':
                    continue
                else:
                    if visit[nx-d[i]][ny-d[3-i]]==-1 or visit[nx-d[i]][ny-d[3-i]]>c+1:
                        q.append((nx-d[i],ny-d[3-i],c+1))
                        visit[nx-d[i]][ny-d[3-i]]=c+1
                    break
    return visit[end[0]][end[1]]