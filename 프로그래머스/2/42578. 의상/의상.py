def solution(clothes):
    d={}
    for i,j in clothes:
        if j in d:
            d[j].append(i)
        else:
            d[j]=[i]
    res=[len(i)+1 for i in d.values()]
    r=1
    for i in res:
        r*=i
    return r-1