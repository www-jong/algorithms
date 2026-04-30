def solution(array):
    d={}
    for i in array:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    li=[]
    for k,v in d.items():
        li.append((k,v))
    li.sort(key=lambda x:-x[1])
    answer = 0
    if len(li)==1:
        return li[0][0]

    return li[0][0] if len(li)>=2 and li[0][1]!=li[1][1] else -1