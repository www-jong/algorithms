def solution(a, b, c, d):
    answer = 0
    s=list(set([a,b,c,d]))
    e=[a,b,c,d]
    if len(s)==1:
        answer=1111*s[0]
    elif len(s)==2:
        if e.count(s[0])==3:
            answer=(10*s[0]+s[1])**2
        elif e.count(s[1])==3:
            answer=(10*s[1]+s[0])**2
        else:
            answer=(s[0]+s[1])*abs(s[0]-s[1])
    elif len(s)==3:
        if e.count(s[0])==2:
            answer=s[1]*s[2]
        elif e.count(s[1])==2:
            answer=s[0]*s[2]
        else:
            answer=s[0]*s[1]
    else:
        answer=min(e)    

    return answer