def solution(s):
    d={}
    answer = []
    for i in s:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for k,v in d.items():
        if v==1:
            answer.append(k)
    return ''.join(sorted(answer))