import heapq
def solution(n, s, a, b, fares):
    def dij(st):
        q=[]
        distance=[float('inf')]*(n+1)
        heapq.heappush(q,(0,st))
        distance[st]=0
        while q:
            dist,now=heapq.heappop(q)
            if distance[now]<dist:
                continue
            for i in graph[now]:
                cost=dist+i[1]
                if cost<distance[i[0]]:
                    distance[i[0]]=cost
                    heapq.heappush(q,(cost,i[0]))
        return distance
    answer = 0
    graph=[[] for _ in range(n+1)]
    for c,d,f in fares:
        graph[c].append((d,f))
        graph[d].append((c,f))
    S=dij(s)
    B=dij(b)
    A=dij(a)
    res=[]
    res.append(S[a]+S[b])
    res.append(S[a]+A[b])
    res.append(S[b]+B[a])
    tmp=float('inf')
    for i in range(1,n+1):
        if i not in {a,b,s}:
            tmp=min(tmp,S[i]+A[i]+B[i])
    res.append(tmp)
    return min(res)