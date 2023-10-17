from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
li=list(map(int,input().split()))
ans=[-1]*(n)
q=deque()
for i in range(n):
    while q and li[q[-1]]<li[i]:
        ans[q.pop()]=li[i]
    q.append(i)
print(*ans)