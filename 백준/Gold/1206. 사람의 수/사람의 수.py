import math
N=int(input())
li=[float(input()) for _ in range(N)]
res=0
def func(n):
    for x in li:
        l,r=0,10*n
        while l<r:
            mid=math.floor((l+r)/2)
            if (mid)/n<x:
                l=mid+1
            else:
                r=mid
        if math.trunc((l/n)*1000)/1000!=x:
            return 0
    return 1
while res<1000:
    res+=1
    if func(res):
        break
print(res)