def solution(n, k, enemy):
    m=len(enemy)
    li=[0]*m
    li[0]=enemy[0]
    for i in range(1,m):
        li[i]=li[i-1]+enemy[i]
    st,end=0,m-1
    res=0
    while st<=end:
        mid=(st+end)//2
        if li[mid]<=n:
            res=max(res,mid)
            st=mid+1
            continue
        tmp=sorted(enemy[:mid+1])[:max(0,mid+1-k)]
        tmp_sum=sum(tmp)
        if tmp_sum<=n:
            res=max(res,mid)
            st=mid+1
        else:
            end=mid-1
    return res+1