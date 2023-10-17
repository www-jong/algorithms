import sys,math
input=sys.stdin.readline
n,m=map(int,input().split())
li=[0]+list(map(int,input().split()))
sums,ex=[0]*(n+1),{}
sums[1]=li[1]
ex[li[1]%m]=1
count=0
for i in range(2,n+1):
    sums[i]=sums[i-1]+li[i]
    if sums[i]%m in ex:
        ex[sums[i]%m]+=1
    else:
        ex[sums[i]%m]=1
count=ex[0] if 0 in ex else 0
for i in ex.keys():
    count+=math.comb(ex[i],2)
print(count)
