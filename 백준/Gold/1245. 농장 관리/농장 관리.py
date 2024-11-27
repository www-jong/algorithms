from collections import deque
def check(x,y):
    return 0<=x<N and 0<=y<M
N,M=map(int,input().split())
d=[[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
li=[list(map(int,input().split())) for _ in range(N)]
visit=[[0]*(M) for _ in range(N)]
res=0
for i in range(N):
    for j in range(M):
        if not visit[i][j]:
            tmp=[(i,j)]
            q=deque()
            q.append((i,j))
            flag=1
            while q:
                x,y=q.popleft()
                for k in range(8):
                    nx,ny=x+d[k][0],y+d[k][1]
                    if check(nx,ny) and (nx,ny) not in tmp:
                        if li[i][j]==li[nx][ny]:
                            q.append((nx,ny))
                            tmp.append((nx,ny))
                        elif li[i][j]<li[nx][ny]:
                            flag=0
                            break
                if not flag:
                    break
            if flag:
                res+=1
                for x,y in tmp:
                    visit[x][y]=1

print(res)