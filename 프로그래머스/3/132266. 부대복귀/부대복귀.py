import heapq
def solution(n, roads, sources, destination):
    answer = []
    graph=[[] for _ in range(n+1)]
    distance=[float('inf') for _ in range(n+1)]
    for a,b in roads:
        graph[a].append(b)
        graph[b].append(a)

    q=[]
    heapq.heappush(q,(0,destination))
    distance[destination]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+1
            if cost<distance[i]:
                distance[i]=cost
                heapq.heappush(q,(cost,i))
    for i in sources:
        answer.append(distance[i] if distance[i]!=float('inf') else -1)
    return answer
