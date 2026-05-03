def solution(board, h, w):
    dir=[0,0,1,-1]
    idx=1
    d={}
    N=len(board)
    li=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] not in d:
                d[board[i][j]]=idx
                idx+=1
            li[i][j]=d[board[i][j]]
    for i in li:
        print(i)
    c=0
    for k in range(4):
        nx,ny=h+dir[k],w+dir[3-k]
        if 0<=nx<N and 0<=ny<N and li[h][w]==li[nx][ny]:
            c+=1
    return c