def solution(grid):
    d=[(-1,0),(0,1),(1,0),(0,-1)]
    answer = []
    N,M=len(grid),len(grid[0])
    li=[[[0]*4 for _ in range(M)] for _ in range(N)]



    for i in range(N):
        for j in range(M):
            for k in range(4):
                if not li[i][j][k]:
                    x,y,v=i,j,k
                    cnt=0
                    while True:
                        li[x][y][v]=1
                        cnt+=1

                        dx,dy=d[v]
                        x,y=(x+dx+N)%N,(y+dy+M)%M
                        if grid[x][y]=='L':
                            v=(v+3)%4
                        elif grid[x][y]=='R':
                            v=(v+1)%4
                        if li[x][y][v]:
                            break
                    answer.append(cnt)
    return sorted(answer)