N=int(input())
li=list(map(int,input().split()))
r=0
t=[]
if N==1:
    li.sort()
    r+=sum(li[:5])
else:
    t.append(min(li[0],li[5]))
    t.append(min(li[1],li[4]))
    t.append(min(li[2],li[3]))
    t.sort()
    m1=t[0]
    m2=t[0]+t[1]
    m3=sum(t)
    n1=4*(N-2)*(N-1)+(N-2)**2
    n2=4*(N-1)+4*(N-2)
    n3=4
    r+=m1*n1
    r+=m2*n2
    r+=m3*n3

print(r)