from collections import deque
def solution(m, n, h, w, drops):
    n,m=m,n
    li=[[10**9]*(m) for _ in range(n)]
    for i in range(len(drops)):
        x,y=drops[i]
        li[x][y]=i+1

    row=[[0]*(m-w+1) for _ in range(n)]
    for x in range(n):
        q=deque()
        for y in range(m):
            while q and li[x][q[-1]]>li[x][y]:
                q.pop()
            q.append(y)
            if q[0]<=y-w:
                q.popleft()
            if y>=w-1:
                row[x][y-w+1]=li[x][q[0]]
        
    col=[[0]*(m-w+1) for _ in range(n-h+1)]
    for y in range(m-w+1):
        q=deque()
        for x in range(n):
            while q and row[q[-1]][y]>=row[x][y]:
                q.pop()
            q.append(x)
            if q[0]<=x-h:
                q.popleft()
            if x>=h-1:
                col[x-h+1][y]=row[q[0]][y]

    res=[0,0,-1]
    for x in range(n-h+1):
        for y in range(m-w+1):
            if col[x][y]>res[2]:
                res=[x,y,col[x][y]]
    return res[:-1]