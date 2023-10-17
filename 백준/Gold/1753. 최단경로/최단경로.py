import heapq
import sys
INF=int(1e9)
V,E=map(int,sys.stdin.readline().split())
start=int(sys.stdin.readline())
graph=[[] for i in range(V+1)]
#graph_cla=[[INF]*(V+1) for i in range(V+1)]
visit=[0]*(V+1)
dist=[INF]*(V+1)
for i in range(E):
    g1,g2,g3=map(int,sys.stdin.readline().split())
    """
    if graph_cla[g1][g2]>g3:
        graph_cla[g1][g2]=g3
for i in range(1,V+1):
    for j in range(1,V+1):
        if graph_cla[i][j]!=INF:
            graph[i].append((j,graph_cla[i][j]))
    """
    graph[g1].append((g2,g3))

def dijkstra(start):
    q=[]
    global dist
    heapq.heappush(q,(0,start))
    dist[start]=0
    while q:
        dists,now=heapq.heappop(q)
        if dist[now]<dists:
            continue
        for i in graph[now]:
            cost=dists+i[1]
            if cost<dist[i[0]]:
                dist[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
                
dijkstra(start)
for i in range(1,V+1):
    if dist[i]==INF:
        print("INF")

    else:
        print(dist[i])