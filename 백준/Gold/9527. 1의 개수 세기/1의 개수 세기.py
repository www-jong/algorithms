import math,sys
sys.setrecursionlimit(10**9)
A,B=map(int,input().split())
res=0
pnum=[0]*(100)
for i in range(1,100):
    pnum[i]=2**(i-1)+2*(pnum[i-1])

def check(n):
    if n<=0:
        return 0

    x=int(math.log2(n)) #   2**x<=n<=2**(x+1)
    if 2**x==n:
        return x*n//2+1
    
    diff=n-2**x
    return check(2**x)+diff+check(diff)
print(check(B)-check(A-1))
    