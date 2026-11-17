n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
d={}
for x,y in points:
    if x in d:
        d[x]=min(d[x],y)
    else:
        d[x]=y
res=0
for k,v in d.items():
    res+=v
print(res)