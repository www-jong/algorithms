def solution(board):
    answer = len(board)**2
    d = [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y]==1:
                answer-=1
                for dx,dy in d:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<len(board) and 0<=ny<len(board) and board[nx][ny]==0:
                        board[nx][ny]=2
                        answer-=1
    return answer