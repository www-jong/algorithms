def solution(k, m, score):
    answer = 0
    score.sort()
    while score:
        c=0
        p=10**9
        while score:
            if score:
                now=score.pop()
                p=min(p,now)
                c+=1
            
            if c==m:
                break
        if c==m:
            answer+=p*c
    return answer