import heapq
def solution(k, score):
    answer = []
    q=[]
    for i in score:
        if len(q)<k:
            heapq.heappush(q,i)
        elif q[0]<i:
            heapq.heappop(q)
            heapq.heappush(q,i)
        answer.append(q[0])
    return answer