from collections import deque
def solution(m, n, h, w, drops):
    INF=len(drops)+1
    li=[[INF]*(n) for _ in range(m)]
    for i,j in enumerate(drops):
        li[j[0]][j[1]]=i
    row=[[0]*(n-w+1) for _ in range(m)]
    for x in range(m):
        q=deque()
        for y in range(n):
            while q and li[x][q[-1]]>=li[x][y]:
                q.pop()
            q.append(y)
            if q[0]<=y-w:
                q.popleft()
            if y>=w-1:
                row[x][y-w+1]=li[x][q[0]]
    
    col=[[0]*(n-w+1) for _ in range(m-h+1)]
    for y in range(n-w+1):
        q=deque()
        for x in range(m):
            while q and row[q[-1]][y]>=row[x][y]:
                q.pop()
            q.append(x)
            if q[0]<=x-h:
                q.popleft()
            if x>=h-1:
                col[x-h+1][y]=row[q[0]][y]
    answer = [0,0,-1]
    for x in range(m-h+1):
        for y in range(n-w+1):
            if col[x][y]>answer[2]:
                answer=[x,y,col[x][y]]
    return answer[:-1]