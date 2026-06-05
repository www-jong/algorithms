def solution(k, tangerine):
    answer = 0
    cnt=0
    d={}
    for i in tangerine:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    li=[(k,v) for k,v in d.items()]
    li.sort(key=lambda x:-x[1])
    for i,j in li:
        answer+=1
        cnt+=j
        if cnt>=k:
            break
    return answer