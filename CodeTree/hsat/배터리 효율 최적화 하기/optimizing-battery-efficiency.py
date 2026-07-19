from itertools import combinations
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
res=-10**9
d=[0,0,1,-1]
cand=set()
def to_1d(x,y):
    return x*M+y

def to_2d(v):
    return v//M,v%M

def func(visit,to_cand):
    if len(visit)==5:
        cand.add(tuple(sorted(visit)))
        return

    for i in list(to_cand):
        if st<i:
            to_cand.discard(i)
            x,y=to_2d(i)
            new_to_cand=to_cand.copy()
            for j in range(4):
                nx,ny=x+d[j],y+d[3-j]
                if 0<=nx<N and 0<=ny<M:
                    v=to_1d(nx,ny)
                    if v not in visit and st<v:
                        new_to_cand.add(v)
            func(visit+[i],new_to_cand)


for x in range(N):
    for y in range(M):
        st=to_1d(x,y)
        to_cand=set()
        for i in range(4):
            nx,ny=x+d[i],y+d[3-i]
            if 0<=nx<N and 0<=ny<M:
                v=to_1d(nx,ny)
                if st<v:
                    to_cand.add(v)
        func([st],to_cand)


for a,b in combinations(cand,2):
    a,b=set(a),set(b)
    #print(a,b)
    if len(a|b)==8:
        val_a,val_b,common=0,0,0
        for i in a:
            x,y=to_2d(i)
            val_a+=grid[x][y]
        for i in b:
            x,y=to_2d(i)
            val_b+=grid[x][y]
        for i in a&b:
            x,y=to_2d(i)
            common+=grid[x][y]
        res=max(res,val_a+val_b)
print(res)