from collections import deque
def solution(players, m, k):
    answer = 0
    print(players,len(players))
    server=[0]*24
    cnt=0
    q=deque()
    for i in range(24):
        while q and i-q[0]>=k:
            q.popleft()
        if players[i]>=m:
            need=players[i]//m
        else:
            continue
        if q and need<=len(q):
            continue
        else:
            for j in range(need-len(q)):
                q.append(i)
                cnt+=1
    return cnt
