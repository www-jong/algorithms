n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

for now in queries:
    st,end=0,len(arr)-1
    c=-1
    while st<=end:
        mid=(st+end)//2
        if arr[mid]==now:
            c=mid+1
            break
        elif arr[mid]<now:
            st=mid+1
        else:
            end=mid-1
    print(c)