import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**7)
N,M=map(int,input().split())
graph=[[] for _ in range(N*2+1)]
for i in range(M):
    x,y=map(int,input().split())
    graph[-x].append(y)
    graph[-y].append(x)

stk=[]
visit=[0]*(2*N+1)
parents=[0]*(2*N+1)
scc_idx=[0]*(2*N+1)

id=1
scc_id=1

def func(now):
    global id,scc_id
    visit[now]=id
    parent=id
    id+=1
    stk.append(now)

    for next in graph[now]:
        if not visit[next]:
            parent=min(parent,func(next))
        elif not parents[next]:
            parent=min(parent,visit[next])

    if parent==visit[now]:
        while stk:
            top=stk.pop()
            parents[top]=1
            scc_idx[top]=scc_id
            if now==top:
                break
        scc_id+=1
    return parent

for i in range(1,2*N+1):
    if not visit[i]:
        func(i)

res=[0]*(N)
for i in range(1,N+1):
    if scc_idx[i]==scc_idx[-i]:
        print(0)
        break
    if scc_idx[i]<scc_idx[-i]:
        res[i-1]=1
else:
    print(1)
    print(*res)
