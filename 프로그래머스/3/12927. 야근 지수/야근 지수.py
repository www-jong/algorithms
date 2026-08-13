import heapq
def solution(n, works):
    answer = 0
    q=[-i for i in works]
    heapq.heapify(q)
    while n and q:
        now=heapq.heappop(q)
        if now!=0:
            heapq.heappush(q,now+1)
        n-=1
    for i in q:
        answer+=(-i)**2
    return answer