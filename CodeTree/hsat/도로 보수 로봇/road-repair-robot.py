N, K = map(int, input().split())
positions = list(map(int, input().split()))
def func(v):
    cnt=1
    st=positions[-1]
    tmp=positions[:-1]
    while tmp:
        now=tmp.pop()
        if st-now+1<=v:
            continue
        else:
            cnt+=1
            st=now
    return cnt

if N==1:
    print(1)
else:
    st,end=1,positions[-1]-positions[0]+1
    res=end
    while st<=end:
        mid=(st+end)//2
        if func(mid)<=K:
            res=mid
            end=mid-1
        else:
            st=mid+1
    print(res)