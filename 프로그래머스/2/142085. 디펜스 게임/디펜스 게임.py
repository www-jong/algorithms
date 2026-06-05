def solution(n, k, enemy):
    if k>=len(enemy):
        return len(enemy)
    res=0
    st,end=0,len(enemy)-1
    t=[0]*(len(enemy))
    t[0]=enemy[0]
    for i in range(1,len(enemy)):
        t[i]=t[i-1]+enemy[i]
    while st<=end:
        mid=(st+end)//2
        if t[mid]<=n:
            res=max(res,mid+1)
            st=mid+1
            continue
        tmp=sorted(enemy[:mid+1])
        v=sum(tmp[:max(len(tmp)-k,0)])
        if v<=n:
            st=mid+1
            res=max(res,mid+1)
        else:
            end=mid-1
    return res