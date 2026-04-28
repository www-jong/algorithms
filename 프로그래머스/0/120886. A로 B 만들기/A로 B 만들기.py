def solution(before, after):
    answer = 0
    d={}
    for i in before:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for i in after:
        if i not in d or d[i]!=after.count(i):
            return 0
    return 1