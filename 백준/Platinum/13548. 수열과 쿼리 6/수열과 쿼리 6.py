from collections import defaultdict
import sys
input=sys.stdin.readline

N=int(input())
sq=N**0.5
li=list(map(int,input().split()))
M=int(input())
query=[]
for idx in range(M):
    i,j=map(lambda x:int(x)-1,input().split())
    query.append((i//sq,i,j,idx))
query.sort(key=lambda x:(x[0],x[2]))

le,ri=0,-1
cnt=defaultdict(int)
dv=[0]*(M+5)
val=0
res=[0]*M
for _,next_le,next_ri,idx in query:
    while le<next_le:
        dv[cnt[li[le]]]-=1
        if dv[cnt[li[le]]]==0 and cnt[li[le]]==val:
            val-=1
        dv[cnt[li[le]]-1]+=1
        cnt[li[le]]-=1
        le+=1

    while next_le<le:
        le-=1
        dv[cnt[li[le]]]-=1
        dv[cnt[li[le]]+1]+=1
        val=max(cnt[li[le]]+1,val)
        cnt[li[le]]+=1

    while ri<next_ri:
        ri+=1
        dv[cnt[li[ri]]]-=1
        dv[cnt[li[ri]]+1]+=1
        val=max(cnt[li[ri]]+1,val)
        cnt[li[ri]]+=1
    while next_ri<ri:
        dv[cnt[li[ri]]]-=1
        if dv[cnt[li[ri]]]==0 and cnt[li[ri]]==val:
            val-=1
        dv[cnt[li[ri]]-1]+=1
        cnt[li[ri]]-=1
        ri-=1
    res[idx]=val

print(*res,sep="\n")