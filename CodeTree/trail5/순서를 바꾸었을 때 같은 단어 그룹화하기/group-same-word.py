n = int(input())
words = [input() for _ in range(n)]

d={}
for word in words:
    a=''.join(sorted([i for i in word]))
    if a in d:
        d[a]+=1
    else:
        d[a]=1
res=0
for k,v in d.items():
    if v>res:
        res=v
print(res)