import sys
input=sys.stdin.readline

def func(now,graph,flag):
    for next in graph[now]:
        if not visit[next]:
            visit[next]=1
            res[flag]+=1
            func(next,graph,flag)

N,M,X=map(int,input().split())
graph1=[[] for _ in range(N+1)]
graph2=[[] for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,input().split())
    graph1[a].append(b)
    graph2[b].append(a)
visit=[0]*(N+1)
res=[0,0]

func(X,graph1,0)
func(X,graph2,1)
print(1+res[1],N-res[0])