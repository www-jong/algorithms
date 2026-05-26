import sys
sys.setrecursionlimit(10 ** 6)

def solution(n, lighthouse):
    def func(now,before):
        for next in graph[now]:
            if len(graph[next])==1 and on[before]==0:
                on[now]=1
                break
        for next in graph[now]:
            if next!=before:
                func(next,now)

                if on[now]==0 and on[next]==0:
                    on[now]=1

    graph=[[] for _ in range(n+1)]
    for a,b in lighthouse:
        graph[a].append(b)
        graph[b].append(a)

    on=[0]*(n+1)
    func(1,0)
    return sum(on)