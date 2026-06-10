from collections import deque
def solution(queue1, queue2):
    q1,q2=deque(queue1),deque(queue2)
    r1,r2=sum(q1),sum(q2)
    if (r1+r2)%2!=0:
        return -1
    answer=0
    v=len(q1)+len(q2)
    while True:
        if answer>v*2:
            return -1
        if r1>r2:
            now=q1.popleft()
            q2.append(now)
            r1-=now
            r2+=now
        elif r1<r2:
            now=q2.popleft()
            q1.append(now)
            r1+=now
            r2-=now
        else:
            return answer
        answer+=1
    
    return answer