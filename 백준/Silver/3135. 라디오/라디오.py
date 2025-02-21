a,b=map(int,input().split())
N=int(input())
li=[int(input()) for i in range(N)]
tmp1,tmp2=[],[]
tmp1.append(abs(a-b))
for i in range(len(li)):
    tmp2.append(abs(li[i]-b))
if abs(a-b)<=min(tmp2):
    print(abs(a-b))
else:
    print(min(tmp2)+1)