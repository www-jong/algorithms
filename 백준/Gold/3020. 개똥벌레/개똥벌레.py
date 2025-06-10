import sys
input=sys.stdin.readline
N,H=map(int,input().split())
dp1=[0]*(H+1)
dp2=[0]*(H+1)
for i in range(N):
    h=int(input())
    if i%2:
        dp1[h]+=1
    else:
        dp2[h]+=1
tmp1,tmp2=[0]*(H+1),[0]*(H+1)
for i in range(H-1,0,-1):
    tmp1[i]+=dp1[i]+tmp1[i+1]
    tmp2[i]+=dp2[i]+tmp2[i+1]
tot=[0]*(H+1)
res=[10**9,0]
for i in range(1,H+1):
    tot[i]+=tmp1[i]+tmp2[H-i+1]
    if tot[i]<res[0]:
        res=[tot[i],1]
    elif tot[i]==res[0]:
        res[1]+=1
print(*res)