n, m = map(int, input().split())
points = list(map(int, input().split()))
segments = [tuple(map(int, input().split())) for _ in range(m)]
points.sort()

for a,b in segments:
    st,end=0,n
    while st<end:
        mid=(st+end)//2
        if points[mid]>=a:
            end=mid
        else:
            st=mid+1
    r1=st
    st,end=0,n
    while st<end:
        mid=(st+end)//2
        if points[mid]>b:
            end=mid
        else:
            st=mid+1
    r2=st
    print(r2-r1)