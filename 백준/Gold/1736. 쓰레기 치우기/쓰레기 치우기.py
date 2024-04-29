import sys

input= sys.stdin.readline
N,M=map(int,input().split())
li=[list(map(int,input().split())) for _ in range(N)]

def func(x,y,c):
    tmp=False
    for i in range(x,N):
        for j in range(y,M):
            if li[i][j]==1:
                li[i][j]=0
                c=c+1+func(i,j,c)
                tmp=True
            if tmp:
                break
        if tmp:
            break
    return c

r=1
for i in range(N+2):
    if r==0:
        print(i-1)
        break
    r=func(i,0,0)