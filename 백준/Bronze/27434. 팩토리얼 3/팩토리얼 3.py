res=1
n=int(input())
if n==0:
    print(1)
else:
    for i in range(1,n+1):
        res*=i
    print(res)