li=[list(map(int,input().split())) for _ in range(4)]
r=0
for i in range(4):
    r+=sum(li[i][:i+1])
print(r)