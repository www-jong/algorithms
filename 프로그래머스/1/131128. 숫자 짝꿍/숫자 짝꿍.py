def solution(X, Y):
    answer = ''
    d1,d2={},{}
    for i in X:
        if i in d1:
            d1[i]+=1
        else:
            d1[i]=1
    for i in Y:
        if i in d2:
            d2[i]+=1
        else:
            d2[i]=1
    d3={}
    for k,v in d1.items():
        if k in d2:
            d3[k]=min(v,d2[k])
    print(d3)
    li=[(int(k),v) for k,v in d3.items()]
    li.sort(key=lambda x:-x[0])
    print(li)
    if not li:
        return "-1"
    if len(li)==1 and li[0][0]==0:
        return "0"
    for x,y in li:
        answer+=str(x)*y
    return answer