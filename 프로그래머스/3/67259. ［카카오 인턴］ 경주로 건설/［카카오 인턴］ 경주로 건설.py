import heapq
def solution(board):
    answer = 0
    N=len(board)
    li=[[[10**9]*4 for _ in range(N)]for _ in range(N)]
    d=[0,0,1,-1]
    q=[(0,0,0,-1)]
    while q:
        cost,x,y,c=heapq.heappop(q)
        if c!=-1 and cost>li[x][y][c]:
            continue
        if x==N-1 and y==N-1:
            return cost
        for i in range(4):
            nx,ny=x+d[i],y+d[3-i]
            if not (0<=nx<N and 0<=ny<N) or board[nx][ny]==1:
                continue
            if c==-1 or c==i:
                new_cost=cost+100
            else:
                new_cost=cost+600

            if new_cost<li[nx][ny][i]:
                li[nx][ny][i] = new_cost
                heapq.heappush(
                    q,(new_cost, nx, ny, i)
                )

    return -1