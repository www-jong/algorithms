from collections import deque
def solution(priorities, location):
    answer = 0
    q=deque()
    N=len(priorities)
    r=[]
    tmp=sorted(priorities[::])
    for i in range(N):
        q.append((i,priorities[i]))
    
    while q:
        idx,now=q.popleft()
        if now==tmp[-1]:
            tmp.pop()
            r.append(idx)
            continue
        q.append((idx,now))
    return r.index(location)+1