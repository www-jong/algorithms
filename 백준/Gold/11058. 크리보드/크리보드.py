N=int(input())
res=[i for i in range(N+1)]
for i in range(6,N+1):
    res[i]=max(res[i-3]*2,res[i-4]*3,res[i-5]*4)
print(res[-1])