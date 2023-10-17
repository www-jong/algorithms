import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
N=int(input())
M=int(input())

cnt=0
weight=0
li=[]
nodes=[i for i in range(N+1)]
def find(a):
    if a==nodes[a]:
        return a
    else:
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

for _ in range(M):
    A,B,C=map(int,input().split())
    li.append([A,B,C])
li.sort(key=lambda x:x[2])
i=0
while cnt<N-1:
    a,b,c=li[i]
    if find(a)!=find(b):
        cnt+=1
        weight+=c
        union(a,b)
    i+=1

print(weight)