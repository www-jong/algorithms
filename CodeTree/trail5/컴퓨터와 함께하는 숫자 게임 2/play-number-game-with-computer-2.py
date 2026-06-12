m = int(input())
a, b = map(int, input().split())
res=[10**9,0]

for i in range(a,b+1):
    cnt=0
    st,end=1,m
    while st<=end:
        cnt+=1
        mid=(st+end)//2
        if mid==i:
            break
        elif mid<i:
            st=mid+1
        else:
            end=mid-1
    res=[min(res[0],cnt),max(res[1],cnt)]
print(*res)

# Please write your code here.
