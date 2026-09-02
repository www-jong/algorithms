def solution(n, times):
    answer = 0
    st,end=min(times),max(times)*n
    
    while st<=end:
        mid=(st+end)//2
        tmp=0
        for i in times:
            tmp+=mid//i
            if tmp>=n:
                break
                
        if tmp>=n:
            answer=mid
            end=mid-1
        else:
            st=mid+1
    return answer