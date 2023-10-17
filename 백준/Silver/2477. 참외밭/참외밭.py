k=int(input())
li=[]
m=[0]*4
for i in range(6):
    q,w=map(int,input().split())
    li.append([q,w])
    m[q-1]+=w

ri=[-2,1,3]
check=0
temp=0

for i,(q,w) in enumerate(li):
    if q-li[i+1 if i!=5 else 0][0] in ri:
        li[i].append(0)
        temp+=0
    else:
        li[i].append(1)
        temp+=1
if temp>2:
    temp=0
else:
    temp=1
for i in range(6):
    if li[i][2]==temp:
        check=li[i][1]*li[i+1 if i!=5 else 0][1]
        break
print((max(m)*min(m)-check)*k)