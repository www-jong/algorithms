from collections import deque
def solution(n, edge):
    answer = 0
    graph=[[] for _ in range(n+1)]
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    v=0
    q=deque()
    q.append(1)
    visit=[-1]*(n+1)
    visit[1]=0
    while q:
        now=q.popleft()
        for i in graph[now]:
            if visit[i]==-1 or visit[i]>visit[now]+1:
                q.append(i)
                v=max(v,visit[now]+1)
                visit[i]=visit[now]+1
    for i in visit:
        if i==v:
            answer+=1
    return answer
