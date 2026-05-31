from collections import deque
def solution(x, y, n):
    answer = 0
    visit=set()
    q=deque()
    visit.add(x)
    q.append((x,0))
    while q:
        x,c=q.popleft()
        if x==y:
            return c
        if x+n not in visit and x+n<=y:
            visit.add(x+n)
            q.append((x+n,c+1))
        if x*2 not in visit and x+n<=y:
            visit.add(x*2)
            q.append((x*2,c+1))
        if x*3 not in visit and x+n<=y:
            visit.add(x*3)
            q.append((x*3,c+1))
    return -1