N = int(input())
S = input()
li=[]
before=-1
for i in range(N):
    if S[i]=='1':
        if before==-1:
            before=i
            continue
        li.append(i-before)
        before=i
li.sort()
now=li.pop()
li.append(now//2)
li.append(now//2+now%2)
print(min(li))