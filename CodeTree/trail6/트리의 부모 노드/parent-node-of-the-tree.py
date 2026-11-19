import sys
input=sys.stdin.readline
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

graph=[[] for _ in range(n+1)]
for a,b in edges:
    graph[a].append(b)
    graph[b].append(a)

parents=[i for i in range(n+1)]
visit=[0]*(n+1)
visit[1]=1
q=[1]
while q:
    now=q.pop()
    for i in graph[now]:
        if not visit[i]:
            parents[i]=now
            visit[i]=1
            q.append(i)
print(*parents[2:],sep="\n")