def solution(s):
    answer=0
    d={}
    c=0
    for i in s:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
        c+=1
        for k,v in d.items():
            if c-v==v:
                answer+=1
                c=0
                d={}
    if d:
        answer+=1
    return answer