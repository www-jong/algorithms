import sys
input=sys.stdin.readline
N=int(input())
li=list(map(int,input().split()))
li.sort()
r=0
for i in range(N):
    r+=(2**(i)-2**(N-i-1))*li[i]
    r%=1000000007
print(r)