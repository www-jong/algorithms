import sys
input=sys.stdin.readline

N=int(input())
s=set()
res=0
for i in range(N):
    a,b=map(int,input().split())
    if b==1:
        if a in s:
            res+=1
        s.add(a)
    else:
        if a not in s:
            res+=1
        else:
            s.remove(a)
res+=len(s)
print(res)