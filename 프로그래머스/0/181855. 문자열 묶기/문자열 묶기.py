def solution(strArr):
    d={}
    for i in strArr:
        if len(i) in d:
            d[len(i)]+=1
        else:
            d[len(i)]=1
    answer = max([i for i in d.values()])
    return answer