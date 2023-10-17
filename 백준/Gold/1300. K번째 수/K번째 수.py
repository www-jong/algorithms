N=int(input())
k=int(input())

start=0
end=N*N
ans=0
while start<=end:
    mid=(start+end)//2
    count=0
    for i in range(1,N+1):
        count+=N if (mid//i)>N else mid//i
    if count>=k:
        ans=mid
        end=mid-1
    elif count<k:
        start=mid+1
print(ans)