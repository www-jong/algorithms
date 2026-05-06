def func(x,y):
    y1,w1,d1=x.split(".")
    y2,w2,d2=y.split(".")
    a=int(y1)*336+int(w1)*28+int(d1)
    b=int(y2)*336+int(w2)*28+int(d2)
    return (a-b)/28
def solution(today, terms, privacies):
    d={}
    for i in terms:
        a,b=i.split()
        d[a]=int(b)
    print(d)
    answer = []
    for i,j in enumerate(privacies):
        a,b=j.split()
        c=func(today,a)
        print(c,d[b])
        if c>=d[b]:
            answer.append(i+1)
        pass
    return answer