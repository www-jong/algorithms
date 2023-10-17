N=int(input())
li=list(map(int,input().split()))
nowmax=li[0]
sample=[0]
maxlen=0
for i in range(len(li)):
    nownum=li[i]
    if sample[-1]<nownum:
        sample.append(nownum)
    else:
        left=0
        right=len(sample)
        while left<right:
            mid=(left+right)//2
            if sample[mid]<nownum:
                left=mid+1
            else:
                right=mid
        sample[right]=nownum
print(len(sample)-1)