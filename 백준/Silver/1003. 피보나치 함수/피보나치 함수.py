a=int(input())
d=[0,1,1,2]
p=[1,0,1,1]
for i in range(4,42):
    d.append(d[i-1]+d[i-2])
    p.append(p[i-1]+p[i-2])
for i in range(1,a+1):
    a=int(input())
    print("%d %d"%(p[a],d[a]))