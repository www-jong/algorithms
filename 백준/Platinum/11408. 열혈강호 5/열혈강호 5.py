from collections import deque
import sys
input=sys.stdin.readline
INF=float('inf')


def func():
    tot_flow,tot_cost=0,0
    while True:
        dist=[INF]*SIZE
        parent=[-1]*SIZE
        edge_idx=[-1]*SIZE
        inq=[0]*SIZE
        dist[0]=0
        q=deque([0])
        inq[0]=1
        while q:
            now=q.popleft()
            inq[now]=0
            for i in range(len(graph[now])):
                next,cap,c,rev=graph[now][i]
                if cap>0 and dist[next]>dist[now]+c:
                    dist[next]=dist[now]+c
                    parent[next]=now
                    edge_idx[next]=i
                    if not inq[next]:
                        q.append(next)
                        inq[next]=1
        if parent[sink]==-1:
            break
        tot_flow+=1
        b=sink
        while b!=source:
            a=parent[b]
            idx=edge_idx[b]
            rev_idx=graph[a][idx][3]
            graph[a][idx][1]-=1
            graph[b][rev_idx][1]+=1
            tot_cost+=graph[a][idx][2]
            b=a
    return tot_flow,tot_cost
def add_edge(u,v,cap,c):
    graph[u].append([v,cap,c,len(graph[v])])
    graph[v].append([u,0,-c,len(graph[u])-1])
N,M=map(int,input().split())
SIZE=N+M+2
source,sink=0,N+M+1
graph=[[] for _ in range(SIZE)]

for i in range(1,N+1):
    add_edge(0,i,1,0)
for i in range(1,M+1):
    add_edge(N+i,sink,1,0)
for i in range(1,N+1):
    tmp=list(map(int,input().split()))
    for j in range(tmp[0]):
        x,y=tmp[2*j+1],tmp[2*j+2]
        add_edge(i,N+x,i,y)

print(*func(),sep="\n")