import math

def comb(n,r):
    return math.factorial(n)//(math.factorial(r)*math.factorial(n-r))

N=int(input())

dp=[[0]*14 for _ in range(N+1)]
dp[0][0]=1
for i in range(N):
    for j in range(13):
        for k in range(4):
            if i+k<=N:
                dp[i+k][j+1]+=dp[i][j]*comb(4,k)

idx=1
res=0
while 4*idx<=N:
    t=comb(13,idx)
    res+=t*dp[N-4*idx][13-idx]
    res%=10007
    idx+=1
print(res%10007)