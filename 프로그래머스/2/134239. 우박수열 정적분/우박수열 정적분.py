def solution(k, ranges):
    answer = []
    d=[k]
    while k!=1:
        if k%2==0:
            k//=2
            d.append(k)
        else:
            k=k*3+1
            d.append(k)
    N=len(d)
    li=[0]*(N+1)
    for i in range(2,N+1):
        li[i]=li[i-1]+(d[i-1]+d[i-2])/2
    for i in ranges:
        a,b=i[0]+1,i[1]+N
        answer.append(li[b]-li[a] if a<=b else -1.0)
    
    return answer