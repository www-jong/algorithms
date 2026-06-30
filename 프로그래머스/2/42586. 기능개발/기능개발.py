from collections import deque
def solution(progresses, speeds):
    answer = []
    q=deque(progresses)
    s=deque(speeds)
    while q:
        idx=0
        
        while q and q[0]>=100:
            idx+=1
            q.popleft()
            s.popleft()
        q=deque([q[i]+s[i] for i in range(len(q))])
        if idx:
            answer.append(idx)
    return answer