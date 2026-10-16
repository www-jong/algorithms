from collections import deque
def solution(n, m, x, y, r, c, k):
    def canMoved(x,y,cnt):
        dist=abs(x-r)+abs(y-c)
        remain=k-cnt
        return dist<=remain and (remain-dist)%2==0
    if not canMoved(x,y,0):
        return 'impossible'
    answer = ''
    d=[(1,0),(0,-1),(0,1),(-1,0)] # dlru
    dr='dlru'
    for cnt in range(1, k+1):
        for i in range(4):
            nx, ny = x+d[i][0], y+d[i][1]

            if 1<=nx<=n and 1<=ny<=m and canMoved(nx,ny,cnt):
                answer += dr[i]
                x, y = nx, ny
                break
    return answer