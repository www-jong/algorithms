def solution(sizes):
    r=[0,0]
    for i in sizes:
        a,b=min(i),max(i)
        r[0]=max(a,r[0])
        r[1]=max(b,r[1])
    answer=r[0]*r[1]
    return answer