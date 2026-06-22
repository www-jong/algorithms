from collections import deque
def solution(N, road, K):
    answer = 0
    graph=[[] for _ in range(N+1)]
    for a,b,c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))
    visit=[-1]*(N+1)
    visit[1]=0
    q=deque()
    q.append((1,0))
    while q:
        x,c=q.popleft()
        for y,t in graph[x]:
            if (visit[y]==-1 or visit[y]>c+t) and c+t<=K:
                visit[y]=c+t
                q.append((y,c+t))

    return sum([1 for i in visit if i!=-1])