import sys,heapq
input=sys.stdin.readline
def addTime(before,cooltime):
    return 1+before+(cooltime-before)%M

def addTime2(before,cooltime):
    bb=before%M
    bb=M if bb==0 else bb
    if bb<cooltime:return before+(cooltime-bb)
    elif bb==cooltime:return before
    else:return before+(cooltime-bb)+M

INF=float('inf')
N,M=map(int,input().split())
g=[[] for _ in range(1+N)]
for i in range(M):
    a,b=map(int,input().split())
    g[a].append((b,i))
    g[b].append((a,i))

distance=[INF]*(N+1)
q=[]
heapq.heappush(q,(0,1))
distance[1]=0
while q:
    dist,now=heapq.heappop(q)
    if now==N:
        break
    if distance[now]<dist:
        continue
    for next,next_time in g[now]:
        cost=addTime(dist,next_time)
        if cost<distance[next]:
            distance[next]=cost
            heapq.heappush(q,(cost,next))
print(distance[N])
