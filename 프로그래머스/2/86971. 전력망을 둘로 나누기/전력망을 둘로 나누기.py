from collections import deque
def solution(n, wires):
    res=n
    graph=[[] for _ in range(n+1)]
    
    def func(x):
        visit=[0]*(n+1)
        q=deque()
        q.append(x)
        visit[x]=1
        cnt=1
        while q:
            now=q.popleft()
            for next in graph[now]:
                if not visit[next]:
                    cnt+=1
                    q.append(next)
                    visit[next]=1
        return cnt
        
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)

        
    for a,b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        res=min(res,abs(func(a)-func(b)))
        graph[a].append(b)
        graph[b].append(a)
    return res