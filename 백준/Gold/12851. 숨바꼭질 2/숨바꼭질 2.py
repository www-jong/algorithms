from collections import deque
N,K=map(int,input().split())
li=[0]*(100001)
res=[10**9,0]

q=deque()
q.append((N,0))
while q:
    x,now=q.popleft()
    if x==K:
        if now==res[0]:
            res[1]+=1
        elif now<res[0]:
            res=[now,1]
    for i in (x-1,x+1,x*2):
        if 0<=i<=100000 and (not li[i] or li[i]>now):
            li[i]=li[x]+1
            q.append((i,now+1))
print(res[0])
print(res[1])