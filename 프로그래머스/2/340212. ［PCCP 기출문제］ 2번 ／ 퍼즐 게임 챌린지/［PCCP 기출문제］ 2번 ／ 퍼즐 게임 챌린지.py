def solution(diffs, times, limit):
    st,end=1,max(diffs)
    res=10**9
    while st<=end:
        mid=(st+end)//2
        now=0
        for i in range(len(diffs)):
            if diffs[i]<mid:
                now+=times[i]
            else:
                v=(times[i-1]+times[i])*(diffs[i]-mid)+times[i]
                now+=v
                before_time=v
            if now>limit:
                st=mid+1
                break
        else:
            res=min(res,mid)
            end=mid-1
            
        
    return res