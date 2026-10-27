import heapq
def solution(n, cores):
    m=len(cores)
    if n<=m:
        return n
    st,end=0,min(cores)*(n-m)
    while st<end:
        mid=(st+end)//2
        cnt=m+sum(mid//i for i in cores)
        if cnt>=n:
            end=mid
        else:
            st=mid+1
    
    tmp=n-m-sum((st-1)//i for i in cores)
    for i,j in enumerate(cores,1):
        if st%j==0:
            tmp-=1
            if tmp==0:
                return i