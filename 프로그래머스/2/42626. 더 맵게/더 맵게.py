import heapq
def solution(scoville, K):
    answer = 0
    q=scoville
    heapq.heapify(q)
    while q[0]<K and len(q)>=2:
        a,b=heapq.heappop(q),heapq.heappop(q)
        c=a+b*2
        heapq.heappush(q,c)
        answer+=1
    if q:
        if q[0]>=K:
            return answer
        
    return -1
    