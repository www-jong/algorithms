def solution(stones, k):
    answer = 0
    le,ri=1,max(stones)+1
    while le<ri-1:
        mid=(le+ri)//2
        now=0
        chk=0
        for i in stones:
            if i<mid:
                now+=1
            else:
                now=0
            if now==k:
                chk=1
                break
        if not chk:
            le=mid
        else:
            ri=mid
    return le