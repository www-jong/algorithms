import sys
input=sys.stdin.readline

N=int(input())
li=list(map(int,input().split()))
s=set(li)
K=int(input())
dp=[float('inf') for _ in range(li[-1]*K+2)]

for i in range(1,li[-1]*K+2):
    if i in s:
        dp[i]=1
    else:
        for j in range(1,i//2+1):
            dp[i]=min(dp[i],dp[j]+dp[i-j])
    if dp[i]>K:
        s='holsoon' if i%2==0 else 'jjaksoon'
        print(f'{s} win at {i}')
        break