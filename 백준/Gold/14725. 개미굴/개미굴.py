from collections import deque
N=int(input())
g={}
def find(depth,now):
    if not now:
        return 0
    if now[0] not in depth:
        next=now.popleft()
        depth[next]={}
        find(depth[next],now)
    else:
        next=now.popleft()
        find(depth[next],now)

def p(now,idx):
    for i in sorted(now.keys()):
        print('--'*idx+i)
        p(now[i],idx+1)

for _ in range(N):
    K,*li=input().split()
    li=deque(li)
    find(g,li)
p(g,0)