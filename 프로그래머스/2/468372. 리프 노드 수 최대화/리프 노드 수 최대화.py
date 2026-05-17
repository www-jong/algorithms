def solution(dist_limit, split_limit):
    def func(x):
        limit=dist_limit
        leaf=0
        nodes=1
        for i in x:
            now=min(nodes,limit)
            leaf+=(nodes-now)
            limit-=now
            nodes=now*i

            if limit==0 or nodes==0:
                break
        leaf+=nodes
        return leaf
    li=[]
    a=0
    while 2**a<=split_limit:
        b=0
        while 2**a*3**b<=split_limit:
            li.append((a,b))
            b+=1
        a+=1
    print(li)
    answer=0
    for a,b in li:
        answer=max(answer,func([2]*a+[3]*b))
    return answer