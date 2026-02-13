import sys
input=sys.stdin.readline
N=int(input())
li=[0]+[int(input()) for _ in range(N)]
res=[0]

def func(x):
    visit[x]=1
    if not visit[li[x]]:
        func(li[x])

for i in range(1,N+1):
    visit=[0]*(N+1)
    func(i)
    res.append(sum(visit))

print(res.index(max(res)))