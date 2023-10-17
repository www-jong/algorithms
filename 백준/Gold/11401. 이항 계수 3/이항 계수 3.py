n,k=map(int,input().split())
a,b=1,1
m=1000000007
for i in range(1,n+1):
    if i<=k:
        b*=i
    if i<=(n-k):
        b*=i
    a*=i
    if a>m:a=a%m
    if b>m:b=b%m
def suq(x,y):
    if y==0:
        return 1
    elif y==1:
        return x
    tmp=suq(x,y//2)
    if y%2==0:
        return tmp*tmp%m
    else:
        return tmp*tmp*x%m
print(a*suq(b,m-2)%m)