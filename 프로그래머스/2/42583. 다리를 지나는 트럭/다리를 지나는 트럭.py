from collections import deque
def solution(bridge_length, weight, truck_weights):
    q=deque()
    tot_weight=0
    time=0
    for i in truck_weights:
        time+=1
        while q and tot_weight+i>weight:
            now,c=q.popleft()
            time=now
            tot_weight-=c
        time=max(time,q[-1][0]-bridge_length+1) if q else max(time,1)
        q.append((time+bridge_length,i))
        tot_weight+=i
    while q:
        now,c=q.popleft()
        time=now
    return time