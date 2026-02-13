N=int(input())
li=list(map(int,input().split()))
res=0
while li:
    tmp=set(sorted(li))
    for i in tmp:
        del li[li.index(i)]
    res+=1
print(res)