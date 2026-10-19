def solution(a):
    INF=float('inf')
    answer = 1
    N=len(a)
    a=[INF]+a+[INF]
    min_v=[INF,-1]
    le,ri=[INF]*(N+1),[INF]*(N+2)
    for i in range(1,N+1):
        if min_v[0]>a[i]:
            min_v=[a[i],i]
        le[i]=min(a[i],le[i-1])
        ri[N+1-i]=min(a[N+1-i],ri[N+2-i])
    for i in range(1,N+1):
        if a[i]==min_v:
            continue
        if (min_v[1]<i and ri[i]==a[i])or(i<min_v[1] and le[i]==a[i]):
            answer+=1
    return answer
