import heapq
def solution(k, n, reqs):
    answer = 10**9
    li=[[] for _ in range(k)]
    for x,y,c in reqs:
        li[c-1].append((x,x+y))
    for i in range(k):
        li[i].sort(key=lambda x:[x[0],x[1]])
    wait=[[0]*(n+1) for _ in range(k)] # [i][j]= i번유형에 j명의 상담원이 있을 때, i번유형 하는데 걸리는 최소대기시간
    for i in range(k):
        for agent in range(1,(n-k+1)+1):
            now=0
            q=[]
            for a,b in li[i]:
                if len(q)<agent:
                    heapq.heappush(q,b)
                else:
                    end=heapq.heappop(q)
                    if end>a:
                        rate=end-a
                        now+=rate
                        heapq.heappush(q,end+b-a)
                    else:
                        heapq.heappush(q,b)
            wait[i][agent]=now
    print(wait)
    def func(now,c,v):
        nonlocal answer
        if now==k:
            if c==n:
                answer=min(answer,v)
            return

        rem=n-c-(k-now-1)+1
        
        for i in range(1,rem):
            func(now+1,c+i,v+wait[now][i])
    
    func(0,0,0)
    return answer