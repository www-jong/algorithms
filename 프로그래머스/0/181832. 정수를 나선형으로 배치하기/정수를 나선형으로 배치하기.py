
def solution(n):
    d=[(0,1),(1,0),(0,-1),(-1,0)]
    answer = [[0]*n for _ in range(n)]
    x,y=0,0
    v=1
    dir=0
    while True:
        while True:
            answer[x][y]=v
            v+=1
            if (not 0<=x+d[dir][0]<n) or (not 0<=y+d[dir][1]<n) or answer[x+d[dir][0]][y+d[dir][1]]:
                break
            x,y=x+d[dir][0],y+d[dir][1]
        if v==n**2+1:
            return answer
        dir=(dir+1)%4
        x,y=x+d[dir][0],y+d[dir][1]

    return answer