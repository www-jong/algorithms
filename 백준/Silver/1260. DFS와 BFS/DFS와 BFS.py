from collections import deque
import sys
input=sys.stdin.readline

def func(now):
    for next in graph[now]:
        if not visit[next]:
            visit[next]=1
            dfs.append(next)
            func(next)
N,M,V=map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i.sort()
visit=[0]*(N+1)
visit[V]=1
dfs=[V]
func(V)

bfs=[V]
q=deque()
q.append(V)
visit=[0]*(N+1)
visit[V]=1
while q:
    now=q.popleft()
    for next in graph[now]:
        if not visit[next]:
            q.append(next)
            visit[next]=1
            bfs.append(next)
print(*dfs)
print(*bfs)