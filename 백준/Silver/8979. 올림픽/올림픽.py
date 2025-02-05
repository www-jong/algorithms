import sys
input=sys.stdin.readline

N,K=map(int,input().split())
li=[list(map(int,input().split()))for _ in range(N)]
li.sort(key=lambda x:(-x[1],-x[2],-x[3]))

cnt=1
tmp=[-1,-1,-1]
a=0
while a<N:
    if tmp[0]!=li[a][1] and tmp[1]!=li[a][2] and tmp[2]!=li[a][3]:
        cnt+=1
        tmp=li[a][1:]
    else:
        pass
    if li[a][0]==K:
        print(cnt)
    a+=1