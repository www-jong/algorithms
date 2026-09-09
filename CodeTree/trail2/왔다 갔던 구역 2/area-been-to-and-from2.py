N=int(input())
li=[]
now=0
for i in range(N):
    a,b=input().split()
    a=int(a)
    if b=='L':
        after=now-a
        li.append((after,1))
        li.append((now,-1))
    else:
        after=now+a
        li.append((after,-1))
        li.append((now,1))
    now=after
li.sort(key=lambda x:x[0])
cnt=0
res=0
before=li[0][0]
for a,b in li:
    if cnt>=2:
        res+=(a-before)
    before=a
    cnt+=b
print(res)