def solution(order):
    answer = 0
    q=[]
    N=len(order)
    con=[i for i in range(N,0,-1)]
    idx=0
    while con:
        if con and con[-1]==order[idx]:
            con.pop()
            answer+=1
            idx+=1
        elif q and q[-1]==order[idx]:
            q.pop()
            answer+=1
            idx+=1
        else:
            q.append(con.pop())
    
    while q:
        if q[-1]==order[idx]:
            q.pop()
            answer+=1
            idx+=1
        else:
            break
    return answer