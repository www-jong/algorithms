import sys
input=sys.stdin.readline
d=[[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]#hnm

M,N,H=map(int,input().split())
li=[[] for _ in range(H)]
q=[]
ch=0
for h in range(H):
    for n in range(N):
        tmp=list(map(int,input().split()))
        for m in range(M):
            if tmp[m]==1:q.append((h,n,m))
            elif tmp[m]==0:ch+=1
        li[h].append(tmp)

res=0
while q:
    tos=q
    q=[]
    flag=0
    for now in tos:
        for i in d:
            next=[now[0]+i[0],now[1]+i[1],now[2]+i[2]]
            if 0<=next[0]<H and 0<=next[1]<N and 0<=next[2]<M:
                if li[next[0]][next[1]][next[2]]==0:
                    flag=1
                    li[next[0]][next[1]][next[2]]=1
                    ch-=1
                    q.append(next)
    if flag:
        res+=1
print(-1 if ch else res)