def solution(park, routes):
    d={'N':(-1,0),'S':(1,0),'W':(0,-1),'E':(0,1)}
    answer = []
    N,M=len(park),len(park[0])
    now=[0,0]
    for i in range(N):
        for j in range(M):
            if park[i][j]=='S':
                now=[i,j]
    for i in routes:
        a,b=i.split()
        for j in range(1,int(b)+1):
            nx,ny=now[0]+d[a][0]*j,now[1]+d[a][1]*j
            if not 0<=nx<N or not 0<=ny<M or park[nx][ny]=='X':
                break
            print(now,nx,ny)
        else:
            now=[now[0]+d[a][0]*int(b),now[1]+d[a][1]*int(b)]
    return now