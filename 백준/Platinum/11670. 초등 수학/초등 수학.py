import sys
input=sys.stdin.readline

def func(x):
    if visit[x]:
        return 0
    visit[x]=1
    for i in li[x]:
        if i not in check or func(check[i]):
            check[i]=x
            return 1
    return 0

N=int(input())
li=[]
original=[]
check={}
for _ in range(N):
    a,b=map(int,input().split())
    original.append((a,b))
    li.append([a+b,a-b,a*b])

for i in range(N):
    visit=[0]*N
    func(i)
if len(check)!=N:
    print('impossible')
else:
    for k,v in sorted(check.items(),key=lambda x:x[1]):
        a,b,c=original[v][0],original[v][1],''
        if original[v][0]+original[v][1]==k:
            c='+'
        elif original[v][0]-original[v][1]==k:
            c='-'
        elif original[v][0]*original[v][1]==k:
            c='*'
        print(f'{a} {c} {b} = {k}')