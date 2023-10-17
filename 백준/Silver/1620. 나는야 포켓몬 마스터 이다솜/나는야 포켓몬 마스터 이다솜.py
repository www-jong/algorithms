import sys
input=sys.stdin.readline
N,M=map(int,input().split())
name={}
num={}
for i in range(1,1+N):
    po=input().rstrip()
    name[po]=i
    num[i]=po
for i in range(M):
    tmp=input().rstrip()
    if tmp.isnumeric():
        print(num[int(tmp)])
    else:
        print(name[tmp])