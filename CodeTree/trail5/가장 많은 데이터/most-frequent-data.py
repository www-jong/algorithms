n = int(input())
words = [input() for _ in range(n)]
d={}
for i in words:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
res=['',0]
for k,v in d.items():
    if v>res[1]:
        res=[k,v]
print(res[1])