import sys,heapq
input=sys.stdin.readline
INF=float('inf')
V,E=map(int,input().split())
graph=[[] for _ in range(V+1)]
for _ in range(E):
    u,v,w=map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

def dtra(start,target=-1):
    q=[]
    heapq.heappush(q,(0,start))
    distance=[INF]*(V+1)
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for new_now,dis in graph[now]:
            cost=dist+dis
            if cost<distance[new_now]:
                distance[new_now]=cost
                heapq.heappush(q,(cost,new_now))
    if target==-1:
        return distance
    return distance[target]

g=list(map(int,input().split()))
st=g[0]
comp=dtra(int(input()))
before=0
res=[INF]*(V+1)
res[st]=0
for i in g[1:]:
    c=dtra(st,i)
    if c==INF or st==i:
        continue
    st=i
    res[i]=max(0 if res[i]==INF else res[i],c+before)
    before+=c
check=0
for i in range(1,V+1):
    if res[i]>=comp[i] and res[i]!=INF:
        check=1
        print(i)
        break
if not check:
    print(-1)
# 4 5 0 0 21115 11115