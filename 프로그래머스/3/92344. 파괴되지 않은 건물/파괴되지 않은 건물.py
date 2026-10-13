def solution(board, skill):
    answer = 0
    N,M=len(board),len(board[0])
    diff=[[0]*(M+1) for _ in range(N+1)]

    for type,r1,c1,r2,c2,degree in skill:
        degree*=1 if type==2 else -1
        diff[r1][c1]+=degree
        diff[r1][c2+1]-=degree
        diff[r2+1][c1]-=degree
        diff[r2+1][c2+1]+=degree
        
    for i in range(N):
        for j in range(1,M):
            diff[i][j]+=diff[i][j-1]
    for i in range(1,N):
        for j in range(M):
            diff[i][j]+=diff[i-1][j]
    for i in range(N):
        for j in range(M):
            if board[i][j]+diff[i][j]>0:
                answer+=1
    
    return answer