import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
n,m=map(int,input().split())
res=0
nodes=[i for i in range(n+1)]

def find(a):
    if a==nodes[a]:
        return a
    nodes[a]=find(nodes[a])
    return nodes[a]

def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        if a<b:
            nodes[b]=a
        else:
            nodes[a]=b
res=0
for i in range(1,m+1):
    a,b=map(int,input().split())
    if find(a)!=find(b):
        union(a,b)
    else:
        if res==0:
            res=i
print(res)