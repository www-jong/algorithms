N,K=map(int,input().split())
li=list(map(int,input().split()))

st,end=0,max(li)
while st<end:
    mid=(st+end)//2
    val=0
    for i in li:
        if i>mid:
            val+=(i-mid)
    if val>K:
        st=mid+1
    else:
        end=mid
print(st)