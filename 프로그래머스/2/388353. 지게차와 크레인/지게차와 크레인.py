from collections import deque
def solution(storage, requests):
    def func(w):
        pass
    d=[0,0,1,-1]
    storage=['0'*len(storage[0])]+storage+['0'*len(storage[0])]
    for i in range(len(storage)):
        storage[i]=['0']+list(storage[i])+['0']
    N,M=len(storage),len(storage[0])

    for i in requests:
        if len(i)==1:
            q=deque([(0,0)])
            visit=set()
            visit.add((0,0))
            while q:
                x,y=q.popleft()
                for j in range(4):
                    nx,ny=x+d[j],y+d[3-j]
                    if 0<=nx<N and 0<=ny<M and (nx,ny) not in visit:
                        if storage[nx][ny]=='0':
                            q.append((nx,ny))
                            visit.add((nx,ny))
                        elif storage[nx][ny]==i:
                            storage[nx][ny]='0'
                            visit.add((nx,ny))
        else:
            for x in range(1,N-1):
                for y in range(1,M-1):
                    if storage[x][y]==i[0]:
                        storage[x][y]='0'
    res=0
    for x in range(1,N-1):
        for y in range(1,M-1):
            if storage[x][y]!='0':
                res+=1
    return res