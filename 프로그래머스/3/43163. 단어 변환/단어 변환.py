from collections import deque
def solution(begin, target, words):
    answer = 0
    N=len(begin)
    if target not in words:
        return 0
    q=deque()
    q.append((begin,0))
    while q:
        now,c=q.popleft()
        if now==target:
            answer=c
            break
        for i in words:
            cnt=0
            for j in range(N):
                if now[j]!=i[j]:
                    cnt+=1
            if cnt==1:
                q.append((i,c+1))
    return answer