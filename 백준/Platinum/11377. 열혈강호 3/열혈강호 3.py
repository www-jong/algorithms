import sys
input=sys.stdin.readline

def func(x):
    global t
    if visit[x]:
        return 0
    visit[x]=1
    for i in li[x]:
        if check[i]==-1 or func(check[i]):
            check[i]=x
            return 1
    return 0

N,M,K=map(int,input().split())
li=[]
check=[-1]*(M+1)
res1,res2=0,0
for _ in range(N):
    n,*tmp=map(int,input().split())
    li.append(tmp)

for i in range(N):
    visit=[0]*N
    if func(i):
        res1+=1
    if res1==M:
        break

for i in range(N):
    visit=[0]*N
    if func(i):
        res2+=1
    if res2==K or res1+res2==M:
        break

print(res1+res2)